from django_mysql.models import Model
from django.db import models
from common.consts import CheckerType, LanguageEnum, VerdictResult
from django_mysql.models.fields import JSONField


class Problem(Model):
    CHECKER_TYPE_CHOICES = [(t.value, t.name) for t in CheckerType]

    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    input_desc = models.TextField(blank=True)
    output_desc = models.TextField(blank=True)
    time_limit = models.IntegerField(default=2000, help_text='In ms')
    memory_limit = models.IntegerField(default=262144, help_text='In KB')
    note = models.TextField(blank=True)
    sample_inputs = JSONField(default=list)
    sample_outputs = JSONField(default=list)
    checker_type = models.SmallIntegerField(choices=CHECKER_TYPE_CHOICES)
    checker_code = models.TextField(blank=True)
    visible = models.BooleanField(default=False, db_index=True)

    def __str__(self):
        return self.title

    @property
    def sj_name(self):
        return f'sj_{self.id}'


class Solution(Model):
    VERDICT_CHOICES = [(v.value, v.name) for v in VerdictResult]

    problem = models.ForeignKey(Problem, models.CASCADE, related_name='solutions')
    code = models.TextField()
    lang = models.SmallIntegerField(choices=[(t.value, t.name) for t in LanguageEnum])
    is_model_solution = models.BooleanField(null=True, blank=True, default=None, help_text='use None instead of False')
    verdict = models.SmallIntegerField(choices=VERDICT_CHOICES, default=VerdictResult.AC)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['problem', 'is_model_solution'], name='unique_problem_model_solution'),
        ]
