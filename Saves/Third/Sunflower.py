def Power(desired = 1000):
    if num_items(Items.Sunflower_Seed) < 200:
        Buy(Items.Sunflower_Seed, 400)
    HarvestAll()
    reset = 0
    listSFH = []
    last = 15
    while True:
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
            if desired < num_items(Items.power):
                return
            last = 15
            reset += 1
            if reset > 1:
                for j in listSFH:
                    if j[2] == 7:
                        GoTo(j[0], j[1])
                        harvest()
                        reset = 0
                        if num_items(Items.Sunflower_Seed) < 200:
                            if not Buy(Items.Sunflower_Seed, 400):
                                HarvestAll()
                        break
            listSFH = []
            Home()

Power(100000000000)