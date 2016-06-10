#!/usr/bin/env python
from flask_script import Manager
from flask.ext.script import Command
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db


app = create_app('default')  # todo sys arg for production

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.add_command
class NoseCommand(Command):
    name = 'test'
    help = 'Runs the nose test suite'
    capture_all_args = True

    def run(self, remaining):
        import nose
        nose.run_exit(
            argv=["nosetests"] + remaining
        )


@manager.add_command
class SeedCommand(Command):
    name = 'seed'
    help = 'Seed the atomic lookup models'

    def run(self):
        from app.atomic.seed import seed_all
        seed_all()


if __name__ == '__main__':
    manager.run()
