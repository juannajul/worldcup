from django.contrib import admin
from worldcup.models.teams import Team
from worldcup.models.worldcup_matches import WorldcupMatch
from worldcup.models.worldcup_pools import WorldcupPool
from worldcup.models.pools_matches import PoolMatch
from worldcup.models.worldcup_key_matches import WorldcupKeyMatch
from worldcup.models.pools_key_matches import PoolKeyMatch

admin.site.register(Team)
admin.site.register(WorldcupMatch)
admin.site.register(WorldcupPool)
admin.site.register(PoolMatch)
admin.site.register(WorldcupKeyMatch)
admin.site.register(PoolKeyMatch)