# import os
# import sys
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import os
import unittest

import model
import schema
import testseed

TESTDB = "__TEST.DB"
model.CONFIG['DBNAME'] = TESTDB

model.DBNAME="test.db"

class TestCursor(unittest.TestCase):

    def setUp(self):
        schema.setup(TESTDB)
        schema.run()
        testseed.setup(TESTDB)
        testseed.run()

    def tearDown(self):
        os.remove(TESTDB)

  #  def testMyFunc(self):
  #     self.assertEqual(model.myfunc(5), 25, "function squares its input")

    def testCursor(self):
        with model.OpenCursor() as cur:
            SQL = "CREATE TABLE nonsense(pk INTEGER PRIMARY KEY AUTOINCREMENT, column VARCHAR);"
            cur.execute(SQL)

            SQL = "INSERT INTO nonsense(column) VALUES('testval');"
            cur.execute(SQL)

        with model.OpenCursor() as cur:
            SQL = "SELECT * FROM nonsense;"
            cur.execute(SQL)
            row = cur.fetchone()
            self.assertEqual(row['column'], 'testval', 'committed INSERT matches SELECT.')
        try: 
            with model.OpenCursor() as cur:
                SQL = "INSERT INTO nonsense(column) VALUES('second');"
                cur.execute(SQL)
                raise Exception
        except:
            pass

        with model.OpenCursor() as cur:
            SQL = "SELECT COUNT(*) FROM nonsense;"
            cur.execute(SQL)
            rows = cur.fetchall()
            self.assertEqual(len(rows), 1, "raised exception prevents INSERT commitment.")

    def testAPI(self):
        price = model.apiget("AAPL")
        self.assertEqual(type(price), float, "getprice returns a float")
        self.assertTrue(price > 0.0, "getprice returns positive value")
        model.CONFIG['FAKEPRICE']['stck'] = 35.55
        self.assertFalse(model.apiget('stck') == 35.55, 'api fake price setter')

    def testAccount(self):
        act = model.Account(username="testman", pass_hash="xxxx", balance=0.0)
        act.save()
        with model.OpenCursor() as cur:
            SQL = "SELECT * FROM accounts WHERE username='testman';"
            cur.execute(SQL)
            row = cur.fetchone()
            self.assertEqual(row["balance"], 0.0, "Account.save() works")

        with model.OpenCursor() as cur:
            SQL = "SELECT * FROM accounts WHERE pk=1;"
            cur.execute(SQL)
            carter = model.Account().set_from_row(cur.fetchone())
            self.assertEqual(carter.balance, 10000.0, "Account set from database row")

        carter2 = model.Account().set_from_pk(1)
        self.assertEqual(carter2.username, "carter", "Account set_from_pk")

        positions = carter2.getpositions()
        self.assertEqual(len(positions), 2, "Account getpositions returns list of correct length")
        self.assertEqual(type(positions[0]), model.Position, "Account getpositions returns list with Positions objects")
        self.assertEqual(positions[0].amount, 10, "getpositions populates Positions with data")

        position = carter2.getposition("AAPL")
        self.assertEqual(type(position), model.Position, "Account getpositions returns Position object")
        self.assertEqual(position.amount, 10, "Position populated with data")

        noposition = carter2.getposition("F")
        self.assertEqual(noposition, None, "getposition returns None for non-position.")

        trades = carter2.gettradesfor("AAPL")
        self.assertEqual(len(trades), 1, "gettradesfor returns list")
        self.assertEqual(type(trades[0]), model.Trade, "gettradesfor list is Trades objects")
        notrades = carter2.gettradesfor("F")
        self.assertEqual(notrades, [], "gettradesfor returns empty list for non-traded symbol")

        # alltrades = carter2.gettrades()
        # self.assertEqual(len(alltrades), 2, "gettrades returns list")

    def testPosition(self):
        pos = model.Position(ticker="IBM", amount=5, account_pk=5)
        self.assertEqual(pos.ticker, "IBM", "Position instantiation")
        pos.save()
        self.assertNotEqual(pos.pk, None, "pk set after Position save")

    def testTrade(self):
        tr = model.Trade(ticker="TSLA", volume=-2, price=3.50, account_pk=5)
        self.assertEqual(tr.ticker, "TSLA", "Trade instantiation")
        tr.save()
        self.assertNotEqual(tr.pk, None, "pk set after Trade save")

    def testMakeTrades(self):
        ac = model.Account().set_from_pk(2)
        buyresult = ac.buy("TSLA", 5)
        self.assertTrue(buyresult, "buy returns true on success")
        balance = ac.balance
        self.assertTrue(balance < 10000.00, "buy spends money")

        fpos = ac.getposition("TSLA")
        self.assertEqual(fpos.amount, 5, "buy creates position")

        ftr = ac.gettradesfor("TSLA")
        self.assertEqual(1, len(ftr), "buy creates trade")
        self.assertEqual(5, ftr[0].volume, "buy sets trade volume")

        ac.sell("TSLA", 3)
        self.assertTrue(ac.balance > balance, "sell earns money")
        fpos = ac.getposition("TSLA")
        self.assertEqual(fpos.amount, 2, "sell reduces position")

        ftr = ac.gettradesfor("TSLA")
        self.assertEqual(2, len(ftr), "sell creates trade")
        self.assertEqual(-3, ftr[1].volume, "sell sets negative trade volume")
   
        # reset balance for other tests
        ac.balance = 10000.0
        ac.save()

    # def testBadTrades(self):
    #     ac = model.Account().set_from_pk(2)
    #     buyresult = ac.buy("TSLA", 5000)
    #     self.assertRaises(buyresult, "bad buy returns false")
    

