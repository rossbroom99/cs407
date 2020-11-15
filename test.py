from verispy import VERIS
data_dir = "F:\\unay\\4th\\cs\\sec\\VCDB\\data\\json\\validated"
v = VERIS(json_dir=data_dir)
df = v.json_to_df(verbose=True)
actors = v.enum_summary(df, 'actor')
actors = actors[['enum', 'x']]
actors.columns = ['Actor Type', 'Count']
actors = actors.drop(2)
actors = actors.drop(3)
actors.head()