import os
import re

def create_template(
    env_file: str = '.env',
    env_template_file: str = '.env.template'
):
    if os.path.exists(env_file):
        with open(env_file, 'r') as f:
            env_vars = f.readlines()
        env_template_lines = []
        for line in env_vars:
            # match an entry like: KEY=value
            m = re.match(r'^\s*(\w+)=(.*)', line)
            if m:
                # replace the value with a placeholder
                env_template_lines.append(f'# {m.group(1)}=REPLACE_ME\n')
            else:
                env_template_lines.append(line)
        with open(env_template_file, 'w') as f:
            f.writelines(env_template_lines)
    else:
        print(f'{env_file} not found')