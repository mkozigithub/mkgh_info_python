import contextlib

class Connection:
    def __init__(self):
        self.xid = 0

    def _start_transaction(self):
        print('starting transaction', self.xid)
        rslt = self.xid
        self.xid = self.xid + 1
        return rslt

    def _commit_transaction(self, xid):
        print('committing transaction', xid)

    def _rollback_transaction(self, xid):
        print('rolling back transaction', xid)


class Transaction:
    def __init__(self, conn):
        self.conn = conn
        self.xid = conn._start_transaction()

    def commit(self):
        self.conn._commit_transaction(self.xid)

    def rollback(self):
        self.conn._rollback_transaction(self.xid)


@contextlib.contextmanager
def start_transaction(connection):
    tx = Transaction(connection)

    try:
        yield tx
    except:
        tx.rollback()
        raise

    tx.commit()


def main():
    conn = Connection()
    try:
        with start_transaction(conn) as tx:
            x = 1 + 1
            raise ValueError()
            y = x + 2
            print(f'transaction 0 = {x}, {y}')
    except ValueError:
        print('Oops! Transaction 0 failed.')

    try:
        with start_transaction(conn) as tx:
            x = 1 + 1
            y = x + 2
            print(f'transaction 0 = {x}, {y}')
    except ValueError:
        assert False



if __name__ == "__main__":
    main()