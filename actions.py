from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import sqlite3 as lite


# def getDesc(variety):
#    conn = lite.connect('wine.db')
#    sql = " SELECT description FROM reviews WHERE variety like (?) limit 1"
#    args = ("%"+variety+"%",)
#    cur = conn.execute(sql, args)
#    rows = cur.fetchall()
#    conn.close()
#    return rows


class ActionHelp(Action):
    def name(self):
        return 'action_help'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_help")
        conn = lite.connect('wine.db')
        sql = " SELECT DISTINCT variety FROM reviews limit 10 "
        cur = conn.execute(sql)
        response = cur.fetchall()
        for row in response:
            row = row[0]
            dispatcher.utter_message("{}".format(row))


class ActionVariety(Action):
    def name(self):
        return 'action_variety'

    def run(self, dispatcher, tracker, domain):
        variety = tracker.get_slot('Variety')
        conn = lite.connect('wine.db')
        sql = (" SELECT description FROM reviews WHERE description IS NOT NULL"
               " AND variety like (?) limit 1")
        args = ("%"+variety+"%",)
        cur = conn.execute(sql, args)
        response = cur.fetchall()
        for row in response:
            row = row[0]
            dispatcher.utter_message("{}".format(row))
        conn.close()
        return [SlotSet('Variety', variety)]


class ActionPrice(Action):
    def name(self):
        return 'action_price'

    def run(self, dispatcher, tracker, domain):
        variety = tracker.get_slot('Variety')
        conn = lite.connect('wine.db')
        sql = ("SELECT price FROM reviews WHERE variety like (?) "
               "ORDER BY points DESC limit 5 ")
        args = ("%"+variety+"%",)
        cur = conn.execute(sql, args)
        price_response = cur.fetchall()
        dispatcher.utter_message("Here are the top 5 prices"
                                 " for {}:".format(variety))
        for row in price_response:
            row = row[0]
            dispatcher.utter_message("${}".format(row))
        conn.close()
        return [SlotSet('Variety', variety)]


class ActionCountry(Action):
    def name(self):
        return 'action_country'

    def run(self, dispatcher, tracker, domain):
        variety = tracker.get_slot('Variety')
        conn = lite.connect('wine.db')
        sql = ("SELECT country FROM reviews WHERE country IS NOT NULL AND "
               "variety like (?) "
               "ORDER BY points DESC limit 1")
        args = ("%"+variety+"%",)
        cur = conn.execute(sql, args)
        country_response = cur.fetchall()
        dispatcher.utter_message("{} is from: \n".format(variety))
        dispatcher.utter_message("{}".format(country_response))
        conn.close()
        return [SlotSet('Variety', variety)]


class ActionRating(Action):
    def name(self):
        return 'action_rating'

    def run(self, dispatcher, tracker, domain):
        variety = tracker.get_slot('Variety')
        conn = lite.connect('wine.db')
        sql = ("SELECT DISTINCT points FROM reviews WHERE points IS NOT NULL "
               "AND variety like (?) limit 1")
        args = ("%"+variety+"%",)
        cur = conn.execute(sql, args)
        rating = cur.fetchall()
        for row in rating:
            row = row[0]
            dispatcher.utter_message("{} has a rating"
                                     " of {}".format(variety, row))
        conn.close()
        return [SlotSet('Variety', variety)]
