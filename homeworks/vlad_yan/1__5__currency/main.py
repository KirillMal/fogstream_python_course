"""
Currency exchange rates are indicated according to
available data from the Central Bank of Russia"""
import configparser
import urllib.request
import xml.etree.ElementTree as ET


# read in URL addresses from configuration parameters;
cparser = configparser.ConfigParser()
cparser.read('config.ini')
NAMES_LINK = cparser['URL']['names_link']
EXCHANGERATE_LINK = cparser['URL']['exchangerate_link']


def read_url(link):
    """Read in URL-page content."""
    f = urllib.request.urlopen(link)
    content = f.read()

    return content


def get_exchange_rate(urllink):
    """Create dictionary containing currency exchange rates."""
    currency_info_page = read_url(urllink)

    root = ET.fromstring(currency_info_page)

    descriptions = [desc for desc in root.iter('description')]
    currency_desc = descriptions[-1]

    curr_names_dict = get_currency_names_dict(NAMES_LINK)

    currency_desc = [item for item in currency_desc.text.split('<br>')]
    exchange_rates = {}
    for d in currency_desc[:-1]:
        name, value = d.split('-')
        name, value = name.strip(), float(value.replace(',', '.'))
        exchange_rates[curr_names_dict[name]] = value

    return exchange_rates


def get_currency_nominals_dict(urllink):
    """
    Create dictionary containing currency nominals
    (US dollar - 1, Japanese Yen - 100, South Korean Won - 1000)."""
    currency_list_page = read_url(urllink)
    root = ET.fromstring(currency_list_page)

    currency_names_dict = {}

    items = root.findall('Item')
    for item in items:
        nominal = item.find('Nominal').text
        engname = item.find('EngName').text
        currency_names_dict[engname] = nominal

    return currency_names_dict


def get_currency_names_dict(urllink):
    """
    Create dictionary, that translates currency names
    from rus to eng."""
    currency_list_page = read_url(urllink)
    root = ET.fromstring(currency_list_page)

    currency_names_dict = {}

    items = root.findall('Item')
    for item in items:
        name = item.find('Name').text
        engname = item.find('EngName').text
        currency_names_dict[name] = engname

    return currency_names_dict


def main():
    """Main function."""
    exch_rate = get_exchange_rate(EXCHANGERATE_LINK)
    nominals_dict = get_currency_nominals_dict(NAMES_LINK)

    message = 'Currencies avaliable:\n%s' % '\n'.join(exch_rate.keys())
    print('%s\n%s\n\n' % (message, '-'*79))

    while True:
        name = input('Enter currency name or "q" to quit:')
        if name == 'q':
            break
        message = '%s %s costs: %s rubles' % (nominals_dict[name], name, exch_rate[name])
        print(message)


if __name__ == '__main__':
    main()

"""
Молодец. Хороший код, понятный даже беглым взглядом.
"""