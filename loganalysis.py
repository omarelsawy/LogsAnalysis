#!/usr/bin/env python2.7
import psycopg2

DBNAME = "news"

three_most_popular_articles = """
        select
            articles.title,
            count(*) as total
        from
            articles
            join log on log.path = ('/article/' || articles.slug)
        group by
            articles.title
        order by
            total desc
        limit
            3
        """

most_popular_authors = """
        select
            authors.name,
            count(*) as total
        from
            articles,authors,log
            where log.path = ('/article/' || articles.slug)
            and authors.id = articles.author
        group by
            authors.name
        order by
            total desc
        """

days_with_high_errors = """
        select
            to_char(dayerrors.date, 'FMMonth DD, YYYY'),
            round((dayerrors.count::decimal/dayrequest.count)*100, 1)
            || '%' as percentage
        from
            (select date(time), count(*) from log
                        group by date(time)) as dayrequest,
            (select date(time), count(*) from log
                        where status like '%4%' or status like '%5%'
                        group by date(time)) as dayerrors where
            dayerrors.date = dayrequest.date
            and ((dayerrors.count::decimal
                    /dayrequest.count)*100) > 1 """


def run():
    one()
    two()
    three()


def get(query):
    try:
        db = psycopg2.connect(database=DBNAME)
    except psycopg2.Error as e:
        print('error', e)
    cursor = db.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    db.close()
    return rows


def one():
    print "Q1. What are the most popular three articles of all time?\n"
    rows = get(three_most_popular_articles)
    for row in rows:
        print "%s -- %d views" % (row[0], row[1])


def two():
    print "\nQ2. Who are the most popular article authors of all time?\n"
    rows = get(most_popular_authors)
    for row in rows:
        print "%s -- %d views" % (row[0], row[1])


def three():
    print "\nQ3. On which days did more than 1% of requests lead to errors?\n"
    rows = get(days_with_high_errors)
    for row in rows:
        print "%s -- %s errors" % (row[0], row[1])

run()
