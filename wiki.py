from json import load, dump
import curses
from curses import textpad

articles_path = 'python/wiki.json'
read_articles = lambda: load(open(articles_path))
write_articles = lambda articles: dump(articles, open(articles_path, 'w'))


def edit(stdscr, article):
    articles = read_articles()
    stdscr.clear()
    stdscr.addstr(articles.get(article, ''))
    tb = textpad.Textbox(stdscr)
    tb.edit()
    articles[article] = tb.gather()
    write_articles(articles)
    stdscr.clear()


def main(stdscr):
    def getstr(y, x):
        curses.echo()
        res = stdscr.getstr(y, x)
        curses.noecho()
        return res.decode()

    while 1:
        stdscr.addstr("Available Articles:\n")
        articles = read_articles()
        for k in articles:
            stdscr.addstr(" - {}\n".format(k))
        stdscr.addstr("Select article to edit or enter q to exit:")
        article = getstr(2 + len(articles), 0)
        if article == 'q':
            break
        edit(stdscr, article)


if __name__ == "__main__":
    curses.wrapper(main)
