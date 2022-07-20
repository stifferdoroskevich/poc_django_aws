from django.shortcuts import render
from django.db import connection


def index(request):
    return render(request, 'core/index.html')


def results(request):
    team_ranking = team_rankings()
    return render(request, 'core/results.html', {'team_ranking': team_ranking})


def team_rankings():
    with connection.cursor() as cursor:
        cursor.execute("""
            select et.type_name,
            row_number() over (partition by et.type_name order by ct.total desc) ranking,
            ct.team,
            ct.total,
            coalesce(ct.stage_1,0) stage_1,
            coalesce(ct.stage_2,0) stage_2,
            coalesce(ct.stage_3,0) stage_3,
            coalesce(ct.stage_4,0) stage_4,
		    coalesce(ct.stage_5,0) stage_5,
		    coalesce(ct.stage_6,0) stage_6,
		    coalesce(ct.stage_7,0) stage_7
            from racing.championship_team ct
            inner join racing.event_type et on
            et.id = ct.type_id
            where et.type_name = 'mtb'
            order by ct.type_id, ct.total desc
            """)
        # full_ranking = cursor.fetchall()
        "Returns all rows from a cursor as a dict"
        desc = cursor.description
        return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
        ]
