# Read deez_nutz file to get dictionary of deez nutz replies
deez_nuts_file = open("discord_bot\deez_nuts.txt", "r")

deez_nuts_dict = {}
for i in deez_nuts_file.readlines():
    i = i.strip().split(": ")
    deez_nuts_dict[i[0]] = i[1]

deez_nuts_file.close()

print(deez_nuts_dict)



from googletrans import Translator

translator = Translator()

print(translator.translate('うちのまえにきてください。'))