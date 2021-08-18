from configparser import ConfigParser

data_options = ['provider', 
                'player_id', 
                'player_state', 
                'player_match_stats', 
                'player_position',
                'player_weapons'
                'allplayers_id', 
                'allplayers_state', 
                'allplayers_match_stats', 
                'allplayers_position',
                'allplayers_weapons',
                'map',
                'map_round_wins',
                'round',
                'bomb',
                'phase_countdowns']
payload_config = {} 

with open('/home/felipet/github/csgo-sitting-duck/gamestate_integration_sittingduck.cfg') as cfg: 
    for line in cfg.readlines():
        clean_line = line.strip().replace('"', "").split()
        if clean_line[0] in data_options:
            payload_config[clean_line[0]] = int(clean_line[-1])

