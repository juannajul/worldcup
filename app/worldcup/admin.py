from django.contrib import admin
from worldcup.models.teams import Team
from worldcup.models.worldcup_matches import WorldcupMatch
from worldcup.models.worldcup_pools import WorldcupPool
from worldcup.models.pools_matches import PoolMatch

admin.site.register(Team)
admin.site.register(WorldcupMatch)
admin.site.register(WorldcupPool)
admin.site.register(PoolMatch)