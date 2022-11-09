"""Pools matches serializers."""

# Django rest framework
from email.policy import default
from multiprocessing import pool
from typing_extensions import Required
from rest_framework import serializers

# Models
from worldcup.models.pools_key_matches import PoolKeyMatch
from worldcup.models.teams import Team
from worldcup.models.worldcup_pools import WorldcupPool
from worldcup.models.worldcup_key_matches import WorldcupKeyMatch

# Serializers
from worldcup.serializers.teams import TeamModelSerializer

class PoolKeyMatchModelSerializer(serializers.ModelSerializer):
    """Pool match model serializer."""
    team_1 = TeamModelSerializer(read_only=True)
    team_2 = TeamModelSerializer(read_only=True)

    class Meta:
        model = PoolKeyMatch
        fields = '__all__'
        

class CreatePoolKeyMatchModelSerializer(serializers.ModelSerializer):
    """Create pool match serializer."""
    team_1 = serializers.CharField(max_length=12)
    team_1_goals = serializers.IntegerField()
    team_1_penalty_goals = serializers.IntegerField(default=0)
    team_2 = serializers.CharField(max_length=12)
    team_2_goals = serializers.IntegerField()
    team_2_penalty_goals = serializers.IntegerField(default=0)
    match_number = serializers.IntegerField()
    match_date = serializers.DateTimeField()
    round = serializers.CharField(max_length=24)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = PoolKeyMatch
        fields = '__all__'
    
    def validate(self, data):
        """Verify that key pool doesn´t exists"""
        match_number = data['match_number']
        pool = data['pool']
        print(pool.id)
        pool = WorldcupPool.objects.get(pk=pool.id)
        key_match = PoolKeyMatch.objects.filter(pool=pool, match_number=match_number)
        key_match.delete()
        team_1_goals = data['team_1_goals']
        team_2_goals = data['team_2_goals']
        team_1_penalty_goals = data['team_1_penalty_goals']
        team_2_penalty_goals = data['team_2_penalty_goals']
        if team_1_goals == team_2_goals:
            if team_1_penalty_goals == team_2_penalty_goals:
                raise serializers.ValidationError('No puede haber empate. Definir equipo ganador por penales en caso de empate.')
        if PoolKeyMatch.objects.filter(match_number=data['match_number'], pool=data['pool']).exists():
            match = PoolKeyMatch.objects.get(match_number=data['match_number'], pool=data['pool'])
            match.delete()
        return data
        

    def create(self, data):
        """Create match."""
        team_1_code = data['team_1']
        team_2_code = data['team_2']
        team_1 = Team.objects.get(team_code=team_1_code)
        team_2 = Team.objects.get(team_code=team_2_code)
        data['team_1'] = team_1
        data['team_2'] = team_2
        pool_team_1_goals = data['team_1_goals']
        pool_team_2_goals = data['team_2_goals']
        pool_team_1_penalty_goals = data['team_1_penalty_goals']
        pool_team_2_penalty_goals = data['team_2_penalty_goals']
        team_winner = None
        team_loser = None
        
        # winner team
                    
        if pool_team_1_goals > pool_team_2_goals:
            # Team 1 wins
            team_winner = team_1
            team_loser = team_2
        elif pool_team_1_goals < pool_team_2_goals:
            # Team 2 wins
            team_winner = team_2
            team_loser = team_1
        elif pool_team_1_goals == pool_team_2_goals:
            # Draw
            # Team 1 wins
            if pool_team_1_penalty_goals > pool_team_2_penalty_goals:
                team_winner = team_1
                team_loser = team_2
                # Team 2 wins
            elif pool_team_1_penalty_goals < pool_team_2_penalty_goals:
                team_winner = team_2
                team_loser = team_1   

        data['team_winner'] = team_winner
        data['team_loser'] = team_loser         
        
        data = PoolKeyMatch.objects.create(**data)
        
        return data

class CreateQuarterFinalMatchModelSerializer(serializers.ModelSerializer):
    """Create pool quarter finals matches serializer."""
    
    match_number = serializers.IntegerField(required=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = PoolKeyMatch
        fields = ('match_number', 'user', 'pool')

    def validate(self, data):
        if data['match_number'] < 57:
            raise serializers.ValidationError('Match number must be between 57 and 60')
        elif data['match_number'] > 60:
            raise serializers.ValidationError('Match number must be between 57 and 60')
        if PoolKeyMatch.objects.filter(match_number=data['match_number'], pool=data['pool']).exists():
            match = PoolKeyMatch.objects.get(match_number=data['match_number'], pool=data['pool'])
            match.delete()
        return data

    def create(self, data):
        """Create match."""
        match_number = data['match_number']
        pool_id = data['pool'].id
        pool = WorldcupPool.objects.get(pk=pool_id)
        if match_number == 57:
            winner_match_49 = PoolKeyMatch.objects.get(pool=pool_id, match_number=49)
            winner_match_50 = PoolKeyMatch.objects.get(pool=pool_id, match_number=50)
            data['team_1'] = winner_match_49.team_winner
            data['team_2'] = winner_match_50.team_winner
            data['pool'] = pool
            data['round'] = 'Quarter-finals'
            data['match_date'] = '2022-12-09 11:00:00'
        elif match_number == 58:
            winner_match_53 = PoolKeyMatch.objects.get(pool=pool_id, match_number=53)
            winner_match_54 = PoolKeyMatch.objects.get(pool=pool_id, match_number=54)
            data['team_1'] = winner_match_53.team_winner
            data['team_2'] = winner_match_54.team_winner
            data['pool'] = pool
            data['round'] = 'Quarter-finals'
            data['match_date'] = '2022-12-09 15:00:00'
        elif match_number == 59:
            winner_match_51 = PoolKeyMatch.objects.get(pool=pool_id, match_number=51)
            winner_match_52 = PoolKeyMatch.objects.get(pool=pool_id, match_number=52)
            data['team_1'] = winner_match_51.team_winner
            data['team_2'] = winner_match_52.team_winner
            data['pool'] = pool
            data['round'] = 'Quarter-finals'
            data['match_date'] = '2022-12-10 11:00:00'
        elif match_number == 60:
            winner_match_55 = PoolKeyMatch.objects.get(pool=pool_id, match_number=55)
            winner_match_56 = PoolKeyMatch.objects.get(pool=pool_id, match_number=56)
            data['team_1'] = winner_match_55.team_winner
            data['team_2'] = winner_match_56.team_winner
            data['pool'] = pool
            data['round'] = 'Quarter-finals'
            data['match_date'] = '2022-12-10 15:00:00'
        data = PoolKeyMatch.objects.create(**data)
        return data

class CreateSemiFinalMatchModelSerializer(serializers.ModelSerializer):
    """Create pool semifinal matches serializer."""
    
    match_number = serializers.IntegerField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = PoolKeyMatch
        fields = ('match_number', 'user', 'pool')

    def validate(self, data):
        if data['match_number'] < 61:
            raise serializers.ValidationError('Match number must be between 61 and 62')
        elif data['match_number'] > 62:
            raise serializers.ValidationError('Match number must be between 61 and 62')
        if PoolKeyMatch.objects.filter(match_number=data['match_number'], pool=data['pool']).exists():
            match = PoolKeyMatch.objects.get(match_number=data['match_number'], pool=data['pool'])
            match.delete()
        return data

    def create(self, data):
        """Create match."""
        match_number = data['match_number']
        pool_id = data['pool'].id
        pool = WorldcupPool.objects.get(pk=pool_id)
        if match_number == 61:
            winner_match_57 = PoolKeyMatch.objects.get(pool=pool_id, match_number=57)
            winner_match_58 = PoolKeyMatch.objects.get(pool=pool_id, match_number=58)
            data['team_1'] = winner_match_57.team_winner
            data['team_2'] = winner_match_58.team_winner
            data['pool'] = pool
            data['round'] = 'Semi-finals'
            data['match_date'] = '2022-12-13 15:00:00'
        elif match_number == 62:
            winner_match_59 = PoolKeyMatch.objects.get(pool=pool_id, match_number=59)
            winner_match_60 = PoolKeyMatch.objects.get(pool=pool_id, match_number=60)
            data['team_1'] = winner_match_59.team_winner
            data['team_2'] = winner_match_60.team_winner
            data['pool'] = pool
            data['round'] = 'Semi-finals'
            data['match_date'] = '2022-12-14 15:00:00'
        data = PoolKeyMatch.objects.create(**data)
        return data

class Create3rdPlaceMatchModelSerializer(serializers.ModelSerializer):
    """Create pool 3rd place match."""
    match_number = serializers.IntegerField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = PoolKeyMatch
        fields = ('match_number', 'user', 'pool')
    
    def validate(self, data):
        if data['match_number'] < 63:
            raise serializers.ValidationError('Match number must be 63')
        elif data['match_number'] > 63:
            raise serializers.ValidationError('Match number must be 63')
        if PoolKeyMatch.objects.filter(match_number=data['match_number'], pool=data['pool']).exists():
            match = PoolKeyMatch.objects.get(match_number=data['match_number'], pool=data['pool'])
            match.delete()
        return data
        

    def create(self, data):
        """Create match."""
        match_number = data['match_number']
        pool_id = data['pool'].id
        pool = WorldcupPool.objects.get(pk=pool_id)
        if match_number == 63:
            winner_match_61 = PoolKeyMatch.objects.get(pool=pool_id, match_number=61)
            winner_match_62 = PoolKeyMatch.objects.get(pool=pool_id, match_number=62)
            data['team_1'] = winner_match_61.team_loser
            data['team_2'] = winner_match_62.team_loser
            data['pool'] = pool
            data['round'] = '3rd-Place'
            data['match_date'] = '2022-12-17 11:00:00'
        data = PoolKeyMatch.objects.create(**data)
        return data

class CreateFinalMatchModelSerializer(serializers.ModelSerializer):
    """Create pool final match serializer."""
    match_number = serializers.IntegerField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = PoolKeyMatch
        fields = ('match_number', 'user', 'pool')
    
    def validate(self, data):
        if data['match_number'] < 64:
            raise serializers.ValidationError('Match number must be 64')
        elif data['match_number'] > 64:
            raise serializers.ValidationError('Match number must be 64')
        
        if PoolKeyMatch.objects.filter(match_number=data['match_number'], pool=data['pool']).exists():
            match = PoolKeyMatch.objects.get(match_number=data['match_number'], pool=data['pool'])
            match.delete()
        return data

    def create(self, data):
        """Create match."""
        match_number = data['match_number']
        pool_id = data['pool'].id
        pool = WorldcupPool.objects.get(pk=pool_id)
        if match_number == 64:
            winner_match_61 = PoolKeyMatch.objects.get(pool=pool_id, match_number=61)
            winner_match_62 = PoolKeyMatch.objects.get(pool=pool_id, match_number=62)
            data['team_1'] = winner_match_61.team_winner
            data['team_2'] = winner_match_62.team_winner
            data['pool'] = pool
            data['round'] = 'Final'
            data['match_date'] = '2022-12-18 11:00:00'
        data = PoolKeyMatch.objects.create(**data)
        return data

class SavePoolKeyMatchResultModelSerializer(serializers.ModelSerializer):
    """Save pool match result serializer."""

    team_1_goals = serializers.IntegerField(required=True)
    team_2_goals = serializers.IntegerField(required=True)
    team_1_penalty_goals = serializers.IntegerField(required=True)
    team_2_penalty_goals = serializers.IntegerField(required=True)

    class Meta:
        model = PoolKeyMatch
        fields = (
            'team_1_goals', 'team_2_goals', 
            'team_1_penalty_goals', 'team_2_penalty_goals')
    
    def validate(self, data):
        """Verify that key pool doesn´t exists"""
        team_1_goals = data['team_1_goals']
        team_2_goals = data['team_2_goals']
        team_1_penalty_goals = data['team_1_penalty_goals']
        team_2_penalty_goals = data['team_2_penalty_goals']
        if team_1_goals == team_2_goals:
            if team_1_penalty_goals == team_2_penalty_goals:
                raise serializers.ValidationError('No puede haber empate. Definir equipo ganador por penales en caso de empate.')
        return data

    def update(self, instance, data):
        """Update pool match result."""
        match = instance[0]
        print(match)
        
        print(data)
        team_1_goals = data['team_1_goals']
        team_2_goals = data['team_2_goals']
        team_1_penalty_goals = data['team_1_penalty_goals']
        team_2_penalty_goals = data['team_2_penalty_goals']
        team_1 = match.team_1
        team_2 = match.team_2
        # winner team
                    
        if team_1_goals > team_2_goals:
            # Team 1 wins
            team_winner = team_1
            team_loser = team_2
        elif team_1_goals < team_2_goals:
            # Team 2 wins
            team_winner = team_2
            team_loser = team_1
        elif team_1_goals == team_2_goals:
            # Draw
            # Team 1 wins
            match.penalties = True
            if team_1_penalty_goals > team_2_penalty_goals:
                team_winner = team_1
                team_loser = team_2
                # Team 2 wins
            elif team_1_penalty_goals < team_2_penalty_goals:
                team_winner = team_2
                team_loser = team_1   

        match.team_winner = team_winner
        match.team_loser = team_loser         
        match.team_1_goals = team_1_goals
        match.team_2_goals = team_2_goals
        match.team_1_penalty_goals = team_1_penalty_goals
        match.team_2_penalty_goals = team_2_penalty_goals
        match.save()
        return match

class SetPoolKeyMatchPointsModelSerializer(serializers.Serializer):
    #Set pool match points serializer.
    
    def update(self, instance , data):
        #Set pool match points.
        print(self.data)
        if len(instance) <= 0:
            raise serializers.ValidationError('There are not matches to set points.')
        else:
            for pool_match in instance:
                pool = WorldcupPool.objects.get(id=pool_match.pool.id)
                match_number = pool_match.match_number
                pool_match_points = 0
                worldcup_match = WorldcupKeyMatch.objects.get(match_number=match_number)
                pool_team_1_code = pool_match.team_1.team_code
                pool_team_2_code = pool_match.team_2.team_code
                worldcup_team_1_code = worldcup_match.team_1.team_code
                worldcup_team_2_code = worldcup_match.team_2.team_code
                pool_team_1_goals = pool_match.team_1_goals
                pool_team_1__penalties_goals = pool_match.team_1_penalty_goals
                pool_team_2_goals = pool_match.team_2_goals
                pool_team_2__penalties_goals = pool_match.team_2_penalty_goals
                worldcup_team_1_goals = worldcup_match.team_1_goals
                worldcup_team_1__penalties_goals = worldcup_match.team_1_penalty_goals
                worldcup_team_2_goals = worldcup_match.team_2_goals 
                worldcup_team_2__penalties_goals = worldcup_match.team_2_penalty_goals
                if pool_team_1_code == worldcup_team_1_code and pool_team_2_code == worldcup_team_2_code:
                    if pool_team_1_goals > pool_team_2_goals and worldcup_team_1_goals > worldcup_team_2_goals:
                        # Team 1 wins
                        pool_match_points = 3
                        if pool_team_1_goals == worldcup_team_1_goals and pool_team_2_goals == worldcup_team_2_goals:
                            # Exact result
                            pool_match_points = 5
                    elif pool_team_1_goals < pool_team_2_goals and worldcup_team_1_goals < worldcup_team_2_goals:
                        # Team 2 wins
                        pool_match_points = 3 
                        if pool_team_1_goals == worldcup_team_1_goals and pool_team_2_goals == worldcup_team_2_goals:
                            # Exact result
                            pool_match_points = 5
                    elif pool_team_1_goals == pool_team_2_goals and worldcup_team_1_goals == worldcup_team_2_goals:
                        # Draw
                        # Team 1 wins
                        if pool_team_1__penalties_goals > pool_team_2__penalties_goals and worldcup_team_1__penalties_goals > worldcup_team_2__penalties_goals:
                            pool_match_points = 3
                            if pool_team_1_goals == worldcup_team_1_goals and pool_team_2_goals == worldcup_team_2_goals:
                                # Exact result
                                pool_match_points = 5
                        # Team 2 wins
                        elif pool_team_1__penalties_goals < pool_team_2__penalties_goals and worldcup_team_1__penalties_goals < worldcup_team_2__penalties_goals:
                            pool_match_points = 3
                            if pool_team_1_goals == worldcup_team_1_goals and pool_team_2_goals == worldcup_team_2_goals:
                                # Exact result
                                pool_match_points = 5

                        
                    # Pool
                    print(pool_match_points)
                    pool.points += pool_match_points
                    pool.round_key_points += pool_match_points
                    pool.save()

                    # Pool match
                    pool_match.pool_match_points = pool_match_points
                    pool_match.analized = True
                    pool_match.save()

                    # Worldcup match
                    worldcup_match.analized = True
                    worldcup_match.save()

        return instance
