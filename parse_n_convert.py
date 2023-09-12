# file_location = "./Convergence_Mod_Weapons_IDs.txt"
# # file_location = "/mnt/c/Users/infin/Dropbox/Me/Elden\ Ring\ Backups/Mods/Convergence_Mod_Weapons_IDs.txt"

# with open(file_location, "r") as f:
#     for line in f:
#         print(line)

# # # file_location = os.system("./Convergence_Mod_Weapons_IDs.txt")
# # file_location = os.system("./test.txt")
# # with open(file_location, 'r+') as f:
# #     # lines = f.readlines()
# #     # lines = [line.rstrip() for line in f]
# # #     lines = [line for line in f]
# # # print(lines)
# #     ...

import re


def parse_item_data(file_name):
    with open(file_name, "r") as f:
        item_data = f.readlines()

    item_names = []
    item_ids = []

    for line in item_data:
        match = re.match(r"(.+?) - (.+)", line)
        if match:
            item_names.append(match.group(1))
            match2 = re.match(r"(.+?) - (.+)", match.group(2))
            if match2:
                item_ids.append(match2.group(2))
            else:
                item_ids.append(match.group(2))
        match = re.match(r"(.+?) : (.+)", line)
        if match:
            item_names.append(match.group(1))
            item_ids.append(match.group(2))

    return item_names, item_ids


def convert_to_hex(item_id):
    return hex(int(item_id))[2:].zfill(8)


def export_to_file(item_names, item_ids, output_file):
    with open(output_file, "w") as f:
        for item_name, item_id in zip(item_names, item_ids):
            # dd 00D6FF10 00000001 FFFF0000 FFFFFFFF // Axe Of Epiphany
            f.write(f"dd {convert_to_hex(item_id)} 00000001 FFFF0000 FFFFFFFF // {item_name}\n")


if __name__ == "__main__":
    item_names, item_ids = parse_item_data("./Convergence_Mod_Weapons_Remnants_Spell_Runes_IDs.txt")
    output_file = "./Convergence_Mod_Weapons_Remnants_Spell_Runes_IDs_HEX.txt"

    export_to_file(item_names, item_ids, output_file)

    print("Successfully exported item data to {}.".format(output_file))