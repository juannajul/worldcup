"""Oficial matches serializers."""

# Django rest framework
import math
from tokenize import group
from rest_framework import serializers

# Models
from worldcup.models.worldcup_key_matches import WorldcupKeyMatch
from worldcup.models.teams import Team
from worldcup.models.pools_matches import PoolMatch

# Serializers
from worldcup.serializers.teams import TeamModelSerializer

class WorldcupKeyMatchModelSerializer(serializers.ModelSerializer):
    """Worldcup model serializer."""
    team_1 = TeamModelSerializer(read_only=True)
    team_2 = TeamModelSerializer(read_only=True)

    class Meta:
        model = WorldcupKeyMatch
        fields = '__all__'
        

class CreateWorldcupKeyMatchModelSerializer(serializers.ModelSerializer):
    """Create worldcup serializer."""
    team_1 = serializers.CharField(max_length=12)
    team_2 = serializers.CharField(max_length=12)
    match_number = serializers.IntegerField()
    match_date = serializers.DateTimeField()



    class Meta:
        model = WorldcupKeyMatch
        fields = '__all__'

    def create(self, data):
        """Create match."""
        team_1_code = data['team_1']
        team_2_code = data['team_2']
        team_1 = Team.objects.get(team_code=team_1_code)
        team_2 = Team.objects.get(team_code=team_2_code)
        data['team_1'] = team_1
        data['team_2'] = team_2
        
        data = WorldcupKeyMatch.objects.create(**data)

        return data

class CreateRoundOf16KeyMatchModelSerializer(serializers.ModelSerializer):
    """Create round of 16 serializer."""
    match_number = serializers.IntegerField()

    class Meta:
        model = WorldcupKeyMatch
        fields = ('match_number',)
    
    def validate(self, data):
        if data['match_number'] < 49:
            raise serializers.ValidationError('Match number must be between 49 and 56')
        elif data['match_number'] > 56:
            raise serializers.ValidationError('Match number must be between 49 and 56')

        if WorldcupKeyMatch.objects.filter(match_number=data['match_number']).exists():
            raise serializers.ValidationError('Match number already exists')
        return data

    def create(self, data):
        """Create match."""
        match_number = data['match_number']
        if match_number == 49:
            group_A = Team.objects.filter(group='A')
            group_B = Team.objects.filter(group='B')
            team_1 = group_A[0]
            team_2 = group_B[1]
            match_date = '2022-12-03 11:00:00'
            round = 'Round of 16'
            data['team_1'] = team_1
            data['team_2'] = team_2
            data['match_date'] = match_date
            data['round'] = round
            data = WorldcupKeyMatch.objects.create(**data)
        elif match_number == 50:
            group_C = Team.objects.filter(group='C')
            group_D = Team.objects.filter(group='D')
            team_1 = group_C[0]
            team_2 = group_D[1]
            match_date = '2022-12-03 15:00:00'
            round = 'Round of 16'
            data['team_1'] = team_1
            data['team_2'] = team_2
            data['match_date'] = match_date
            data['round'] = round
            data = WorldcupKeyMatch.objects.create(**data)
        elif match_number == 51:
            group_A = Team.objects.filter(group='A')
            group_B = Team.objects.filter(group='B')
            team_1 = group_B[0]
            team_2 = group_A[1]
            match_date = '2022-12-04 15:00:00'
            round = 'Round of 16'
            data['team_1'] = team_1
            data['team_2'] = team_2
            data['match_date'] = match_date
            data['round'] = round
            data = WorldcupKeyMatch.objects.create(**data)
        elif match_number == 52:
            group_C = Team.objects.filter(group='C')
            group_D = Team.objects.filter(group='D')
            team_1 = group_D[0]
            team_2 = group_C[1]
            match_date = '2022-12-04 11:00:00'
            round = 'Round of 16'
            data['team_1'] = team_1
            data['team_2'] = team_2
            data['match_date'] = match_date
            data['round'] = round
            data = WorldcupKeyMatch.objects.create(**data)
        elif match_number == 53:
            group_E = Team.objects.filter(group='E')
            group_F = Team.objects.filter(group='F')
            team_1 = group_E[0]
            team_2 = group_F[1]
            match_date = '2022-12-05 11:00:00'
            round = 'Round of 16'
            data['team_1'] = team_1
            data['team_2'] = team_2
            data['match_date'] = match_date
            data['round'] = round
            data = WorldcupKeyMatch.objects.create(**data)
        elif match_number == 54:
            group_G = Team.objects.filter(group='G')
            group_H = Team.objects.filter(group='H')
            team_1 = group_G[0]
            team_2 = group_H[1]
            match_date = '2022-12-05 15:00:00'
            round = 'Round of 16'
            data['team_1'] = team_1
            data['team_2'] = team_2
            data['match_date'] = match_date
            data['round'] = round
            data = WorldcupKeyMatch.objects.create(**data)
        elif match_number == 55:
            group_E = Team.objects.filter(group='E')
            group_F = Team.objects.filter(group='F')
            team_1 = group_F[0]
            team_2 = group_E[1]
            match_date = '2022-12-06 11:00:00'
            round = 'Round of 16'
            data['team_1'] = team_1
            data['team_2'] = team_2
            data['match_date'] = match_date
            data['round'] = round
            data = WorldcupKeyMatch.objects.create(**data)
        elif match_number == 56:
            group_G = Team.objects.filter(group='G')
            group_H = Team.objects.filter(group='H')
            team_1 = group_H[0]
            team_2 = group_G[1]
            match_date = '2022-12-06 15:00:00'
            round = 'Round of 16'
            data['team_1'] = team_1
            data['team_2'] = team_2
            data['match_date'] = match_date
            data['round'] = round
            data = WorldcupKeyMatch.objects.create(**data)

        return data


class CreateRoundOf8KeyMatchModelSerializer(serializers.ModelSerializer):
    """Create round of 16 serializer."""
    match_number = serializers.IntegerField()

    class Meta:
        model = WorldcupKeyMatch
        fields = ('match_number',)
    
    def validate(self, data):
        if data['match_number'] < 57:
            raise serializers.ValidationError('Match number must be between 57 and 60')
        elif data['match_number'] > 60:
            raise serializers.ValidationError('Match number must be between 57 and 60')

        if WorldcupKeyMatch.objects.filter(match_number=data['match_number']).exists():
            raise serializers.ValidationError('Match number already exists')
        return data

    def create(self, data):
        """Create match."""
        match_number = data['match_number']
        if match_number == 57:
            round_of_16_match_1 = WorldcupKeyMatch.objects.get(match_number=49)
            round_of_16_match_2 = WorldcupKeyMatch.objects.get(match_number=50)
            team_1 = round_of_16_match_1.team_winner
            team_2 = round_of_16_match_2.team_winner
            match_date = '2022-12-09 11:00:00'
            round = 'Round of 8'
            data['team_1'] = team_1
            data['team_2'] = team_2
            data['match_date'] = match_date
            data['round'] = round
            data = WorldcupKeyMatch.objects.create(**data)
        elif match_number == 58:
            round_of_16_match_1 = WorldcupKeyMatch.objects.get(match_number=53)
            round_of_16_match_2 = WorldcupKeyMatch.objects.get(match_number=54)
            team_1 = round_of_16_match_1.team_winner
            team_2 = round_of_16_match_2.team_winner
            match_date = '2022-12-09 15:00:00'
            round = 'Round of 8'
            data['team_1'] = team_1
            data['team_2'] = team_2
            data['match_date'] = match_date
            data['round'] = round
            data = WorldcupKeyMatch.objects.create(**data)
        elif match_number == 59:
            round_of_16_match_1 = WorldcupKeyMatch.objects.get(match_number=51)
            round_of_16_match_2 = WorldcupKeyMatch.objects.get(match_number=52)
            team_1 = round_of_16_match_1.team_winner
            team_2 = round_of_16_match_2.team_winner
            match_date = '2022-12-10 11:00:00'
            round = 'Round of 8'
            data['team_1'] = team_1
            data['team_2'] = team_2
            data['match_date'] = match_date
            data['round'] = round
            data = WorldcupKeyMatch.objects.create(**data)
        elif match_number == 60:
            round_of_16_match_1 = WorldcupKeyMatch.objects.get(match_number=55)
            round_of_16_match_2 = WorldcupKeyMatch.objects.get(match_number=56)
            team_1 = round_of_16_match_1.team_winner
            team_2 = round_of_16_match_2.team_winner
            match_date = '2022-12-10 15:00:00'
            round = 'Round of 8'
            data['team_1'] = team_1
            data['team_2'] = team_2
            data['match_date'] = match_date
            data['round'] = round
            data = WorldcupKeyMatch.objects.create(**data)

        return data

class CreateSemifinalKeyMatchModelSerializer(serializers.ModelSerializer):
    """Create round of 16 serializer."""
    match_number = serializers.IntegerField()

    class Meta:
        model = WorldcupKeyMatch
        fields = ('match_number',)
    
    def validate(self, data):
        if data['match_number'] < 61:
            raise serializers.ValidationError('Match number must be between 61 and 62')
        elif data['match_number'] > 62:
            raise serializers.ValidationError('Match number must be between 61 and 62')

        if WorldcupKeyMatch.objects.filter(match_number=data['match_number']).exists():
            raise serializers.ValidationError('Match number already exists')
        return data

    def create(self, data):
        """Create match."""
        match_number = data['match_number']
        if match_number == 61:
            round_of_8_match_1 = WorldcupKeyMatch.objects.get(match_number=57)
            round_of_8_match_2 = WorldcupKeyMatch.objects.get(match_number=58)
            team_1 = round_of_8_match_1.team_winner
            team_2 = round_of_8_match_2.team_winner
            match_date = '2022-12-09 11:00:00'
            round = 'Semifinal'
            data['team_1'] = team_1
            data['team_2'] = team_2
            data['match_date'] = match_date
            data['round'] = round
            data = WorldcupKeyMatch.objects.create(**data)
        elif match_number == 62:
            round_of_16_match_1 = WorldcupKeyMatch.objects.get(match_number=59)
            round_of_16_match_2 = WorldcupKeyMatch.objects.get(match_number=60)
            team_1 = round_of_16_match_1.team_winner
            team_2 = round_of_16_match_2.team_winner
            match_date = '2022-12-09 15:00:00'
            round = 'Semifinal'
            data['team_1'] = team_1
            data['team_2'] = team_2
            data['match_date'] = match_date
            data['round'] = round
            data = WorldcupKeyMatch.objects.create(**data)
        
        return data

class CreateFinalKeyMatchModelSerializer(serializers.ModelSerializer):
    """Create round of 16 serializer."""
    match_number = serializers.IntegerField()

    class Meta:
        model = WorldcupKeyMatch
        fields = ('match_number',)
    
    def validate(self, data):
        if data['match_number'] < 63:
            raise serializers.ValidationError('Match number must be between 63 and 64')
        elif data['match_number'] > 64:
            raise serializers.ValidationError('Match number must be between 63 and 64')

        if WorldcupKeyMatch.objects.filter(match_number=data['match_number']).exists():
            raise serializers.ValidationError('Match number already exists')
        return data

    def create(self, data):
        """Create match."""
        match_number = data['match_number']
        if match_number == 63:
            round_semifinal_match_1 = WorldcupKeyMatch.objects.get(match_number=61)
            round_semifinal_match_2 = WorldcupKeyMatch.objects.get(match_number=62)
            team_1 = round_semifinal_match_1.team_loser
            team_2 = round_semifinal_match_2.team_loser
            match_date = '2022-12-09 11:00:00'
            round = '3rd Place'
            data['team_1'] = team_1
            data['team_2'] = team_2
            data['match_date'] = match_date
            data['round'] = round
            data = WorldcupKeyMatch.objects.create(**data)
        elif match_number == 64:
            round_semifinal_match_1 = WorldcupKeyMatch.objects.get(match_number=61)
            round_semifinal_match_2 = WorldcupKeyMatch.objects.get(match_number=62)
            team_1 = round_semifinal_match_1.team_winner
            team_2 = round_semifinal_match_2.team_winner
            match_date = '2022-12-09 15:00:00'
            round = 'Final'
            data['team_1'] = team_1
            data['team_2'] = team_2
            data['match_date'] = match_date
            data['round'] = round
            data = WorldcupKeyMatch.objects.create(**data)
        
        return data

class StartKeyMatchModelSerializer(serializers.Serializer):
    """Start match serializer."""
    def update(self, instance , data):
        """Start match."""
        
        match = instance
        match.started = True
        match.save()
        return instance


class FinishKeyMatchModelSerializer(serializers.Serializer):
    """finish match of round of 16"""
    def update(self, instance , data):
        """Finish match."""
        print(len(instance))
        print(instance)
        if len(instance) > 0:
            match = instance[0] 
            match_number = match.match_number
            data['match'] = match
            team_1 = Team.objects.get(team_code=instance[0].team_1.team_code)
            team_1_goals = match.team_1_goals
            team_1_penalty_goals = match.team_1_penalty_goals
            team_2 = Team.objects.get(team_code=instance[0].team_2.team_code)
            team_2_goals = match.team_2_goals
            team_2_penalty_goals = match.team_2_penalty_goals
            if team_1_goals > team_2_goals:
                # Team 1 wins
                match.finished = True
                match.team_winner = team_1
                match.team_loser = team_2
                match.save()
            elif team_1_goals < team_2_goals:
                # Team 2 wins
                match.finished = True
                match.team_winner = team_2
                match.team_loser = team_1
                match.save()
            elif team_1_goals == team_2_goals:
                # Draw
                match.penalties = True
                if team_1_penalty_goals > team_2_penalty_goals:
                    match.finished = True
                    match.team_winner = team_1
                    match.team_loser = team_2
                    match.save()
                elif team_1_penalty_goals < team_2_penalty_goals:
                    match.finished = True
                    match.team_winner = team_2
                    match.team_loser = team_1
                    match.save()
                elif team_1_penalty_goals == team_2_penalty_goals:
                    raise serializers.ValidationError('Draw not allowed')
            
            pool_matches = PoolMatch.objects.filter(match_number=match_number)
            for pool_match in pool_matches:
                pool_match.finished = True
                pool_match.save() 
            return match
        else:
            raise serializers.ValidationError('there is no match started')
        return match