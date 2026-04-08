from django.test import TestCase
from .models import User, Team, Workout, Activity, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel', description='Marvel Team')
        self.user = User.objects.create(email='ironman@marvel.com', username='IronMan', team=self.team, is_superhero=True)
        self.workout = Workout.objects.create(name='Pushups', description='Upper body', difficulty='Easy')
        self.activity = Activity.objects.create(user=self.user, workout=self.workout, duration=30, calories_burned=100)
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=1000, rank=1)

    def test_user_team(self):
        self.assertEqual(self.user.team.name, 'Marvel')

    def test_activity_workout(self):
        self.assertEqual(self.activity.workout.name, 'Pushups')

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.rank, 1)
