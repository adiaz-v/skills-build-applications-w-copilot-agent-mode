from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Workout, Activity, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Users
        ironman = User.objects.create(email='ironman@marvel.com', username='IronMan', team=marvel, is_superhero=True)
        captain = User.objects.create(email='captain@marvel.com', username='CaptainAmerica', team=marvel, is_superhero=True)
        batman = User.objects.create(email='batman@dc.com', username='Batman', team=dc, is_superhero=True)
        superman = User.objects.create(email='superman@dc.com', username='Superman', team=dc, is_superhero=True)

        # Workouts
        pushups = Workout.objects.create(name='Pushups', description='Upper body', difficulty='Easy')
        squats = Workout.objects.create(name='Squats', description='Lower body', difficulty='Medium')

        # Activities
        Activity.objects.create(user=ironman, workout=pushups, duration=30, calories_burned=100)
        Activity.objects.create(user=batman, workout=squats, duration=45, calories_burned=150)

        # Leaderboard
        Leaderboard.objects.create(user=ironman, score=200, rank=1)
        Leaderboard.objects.create(user=batman, score=180, rank=2)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
