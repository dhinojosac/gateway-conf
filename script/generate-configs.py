import yaml

configs = []

print 'Reading frequency-plans.yml'

f = open('frequency-plans.yml')
frequency_plans = yaml.safe_load(f)
f.close()
for key, frequency_plan in frequency_plans.items():
    if key[0] == '_' or frequency_plan == None:
        continue
    if 'base_freq' not in frequency_plan or 'global_conf' not in frequency_plan or 'description' not in frequency_plan:
        continue
    print 'Adding %s frequency plan' % key
    configs.append('%s:%s:%s' % (frequency_plan['base_freq'], frequency_plan['global_conf'], frequency_plan['description'].replace(' ', '_')))

output = """# List of available configs for installer
# This file is generated by running "make configs.txt"
# baseFreq:filename:Description_no_spaces_allowed
""" + '\n'.join(sorted(configs)) + '\n'

print 'Writing configs.txt'

f = open('configs.txt', 'w')
f.write(output)
f.close()
