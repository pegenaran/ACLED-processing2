regnames_map1 = {'BARMM':'BARMM',
    'CAR':'CAR',
    'I':'Region I',
    'II':'Region II',
    'III':'Region III',
    'IV-A':'Region IV-A',
    'IX':'Region IX',
    'Mimaropa':'Mimaropa',
    'NCR':'NCR',
    'V':'Region V',
    'VI':'Region VI',
    'VII':'Region VII',
    'VIII':'Region VIII',
    'X':'Region X',
    'XI':'Region XI',
    'XII':'Region XII',
    'XIII':'Region XIII'
}

# this is used by the ACLED database and falls under the column header admin1
regnames_map2 = {'Bangsamoro Autonomous Region in Muslim Mindanao':'BARMM',
    'Bicol Region':'Region V',
    'Cagayan Valley':'Region II',
    'Calabarzon':'Region IV-A',
    'Caraga':'Region XIII',
    'Central Luzon':'Region III',
    'Central Visayas':'Region VII',
    'Cordillera Administrative Region':'CAR',
    'Davao Region':'Region XI',
    'Eastern Samar':'Region VIII',
    'Eastern Visayas':'Region VIII',
    'Ilocos Region':'Region I',
    'Mimaropa Region':'Mimaropa',
    'National Capital Region':'NCR',
    'Northern Mindanao':'Region X',
    'Soccsksargen':'Region XII',
    'Western Visayas':'Region VI',
    'Zamboanga Peninsula':'Region IX'
}

noreplace_list = ['BARMM','CAR','NCR']

colstouse = ['event_type','sub_event_type','actor1','assoc_actor_1',
    'actor2','assoc_actor_2','admin1','admin2','admin3','location',
    'latitude','longitude','geo_precision','source','source_scale',
    'notes','fatalities','event_date']
cols_order = ['event_type','sub_event_type','actor1','assoc_actor_1',
    'actor2','assoc_actor_2','comp_act1','comp_assoc_act1','comp_act2',
    'comp_assoc_act2','Region','Province','Municipality','Baranggay',
    'latitude','longitude','geo_precision','source','source_scale',
    'fatalities','notes']

col_renames = {
    'Philippines': {
        'admin2':'Province',
          'admin3':'Municipality',
          'location':'Baranggay'
    }
}

# phildata_stem = 'PhilData/'
phildata_stem = 'Philippines/'