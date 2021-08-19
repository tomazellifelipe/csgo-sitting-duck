from configparser import ConfigParser

def parse_cfg(path, data):
    config = {}
    with open(path) as cfg: 
        for line in cfg.readlines():
            clean_line = line.strip().replace('"', "").split()
            if clean_line[0] in data and clean_line[-1] == '1':
                config[clean_line[0]] = int(clean_line[-1])
    return config

data_options = ['provider', 'player_id', 'player_state', 'player_match_stats', 
                'player_position', 'player_weapons' 'allplayers_id', 'allplayers_state', 
                'allplayers_match_stats', 'allplayers_position', 'allplayers_weapons', 'map',
                'map_round_wins', 'round', 'bomb', 'phase_countdowns']

payload_config = parse_cfg('/home/felipet/github/csgo-sitting-duck/gamestate_integration_sittingduck.cfg', data_options)
print(payload_config)
