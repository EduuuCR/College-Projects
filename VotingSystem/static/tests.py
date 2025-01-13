from django.test import TestCase
from django.contrib.auth.models import User
from .models import Competition, Entry
from datetime import date

class CompetitionModelTest(TestCase):
    def setUp(self):
        self.competition = Competition.objects.create(
            name="Test Competition",
            description="This is a test competition.",
            start_date=date(2025, 1, 1),
            end_date=date(2025, 12, 31),
        )

    def test_competition_creation(self):
        self.assertEqual(self.competition.name, "Test Competition")
        self.assertEqual(self.competition.description, "This is a test competition.")
        self.assertEqual(self.competition.start_date, date(2025, 1, 1))
        self.assertEqual(self.competition.end_date, date(2025, 12, 31))

class EntryModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.competition = Competition.objects.create(
            name="Test Competition",
            description="This is a test competition.",
            start_date=date(2025, 1, 1),
            end_date=date(2025, 12, 31),
        )
        self.entry = Entry.objects.create(
            competition=self.competition,
            user=self.user,
            title="Test Entry",
            description="This is a test entry.",
            votes=0,
        )

    def test_entry_creation(self):
        self.assertEqual(self.entry.title, "Test Entry")
        self.assertEqual(self.entry.description, "This is a test entry.")
        self.assertEqual(self.entry.votes, 0)
        self.assertEqual(self.entry.competition, self.competition)
        self.assertEqual(self.entry.user, self.user)
