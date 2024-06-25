def Power():
	HarvestAll()
    reset = 0
    listSFH = []
    last = 15
    a = 0
    while a < 4:
        if num_items(Items.Sunflower_Seed) < 100:
            if not trade(Items.Sunflower_Seed, 100):
                return

        WaterTill()
        plant(Entities.Sunflower)
                
        listSFH.append([get_pos_x(), get_pos_y(), measure()])
        Next()

        if not get_pos_x() and not get_pos_y():
            while last > 8:
                for i in listSFH:
                    if i[2] == last:
                        GoTo(i[0], i[1])
                        harvest() 
                last -= 1
            last = 15
            reset += 1
            if reset > 1:
                for j in listSFH:
                    if j[2] == 7:
                        GoTo(j[0], j[1])
                        harvest()
                        a += 1
                        reset = 0
                        break
            listSFH = []
            Home()
while True:
	Power()