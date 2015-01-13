__author__ = 'hd'

from jinja2 import Markup


class MomentJS(object):

    def __init__(self, timestamp):
        self.timestamp = timestamp

    def render(self, str_format):
        return Markup("<script>\ndocument.write(moment(\"{0}\").{1});\n</script>".format(
            self.timestamp.strftime("%Y-%m-%dT%H:%M:%S Z"), str_format))

    def format(self, fmt):
        return self.render("format(\"{0}\")".format(fmt))

    def calendar(self):
        return self.render("calendar()")

    def from_now(self):
        return self.render("fromNow()")

