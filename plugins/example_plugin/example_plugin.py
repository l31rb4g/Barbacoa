import urllib2


class ExamplePlugin:

    def get_my_ip(self):
        my_ip = urllib2.urlopen('htp://paladino.pro/ip.php').readline().strip()
        return my_ip