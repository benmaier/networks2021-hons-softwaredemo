import tacoma as tc

model = tc.FlockworkPModel([],200,gamma=1,P=0.5)
model.simulate(200,save_temporal_network=True)

tc.write_json_taco(model.edge_changes, './fw_exmpl.json')
