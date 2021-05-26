import os
import skimage.io as io

# Dictionnaires des coordonnées du caryotype
data = {"c1": (19,138,173,266), 
    "c2": (211,136,353,267), 
    "c3": (294,136,534,268), 
    "c4":(734,153,862,268), 
    "c5":(937,158,1039,267),
    "c6":(32,370,137,470),
    "c7": (179,365,295,472), 
    "c8": (334,365,448,472),
    "c9":(485,369,608,474),
    "c10":(641,365,750,472),
    "c11":(795,365,912,470), 
    "c12":(949,362,1059,473), 
    "c13":(21,557,150,653),
    "c14":(185,561,291,655), 
    "c15":(335,558,448,653),
    "c16":(641,569,742,653), 
    "c17":(796,567,899,653), 
    "c18":(951,562,1051,653), 
    "c19":(38,764,147,858),
    "c20":(185,757,301,860),
    "c21":(417,757,525,857),
    "c22":(573,760,675,859),
    "cx":(781,744,920,855),
    "cy":(945,741,1063,859)}

# Fonction pour récupérer toutes les images de chromosomes d'un caryotype
def crop_chromosomes(path, name, img, coord):
    for k, v in coord.items():
        save_path = os.path.join(path.split("/")[0], "cropped")
        if not os.path.exists(os.path.join(save_path, k)):
            os.makedirs(os.path.join(save_path, k))
            print(f"Directory {k} created")
        io.imsave(os.path.join(save_path, k, f"{'.'.join(name.split('.')[0:2])}.png"), img[v[1]:v[3], v[0]:v[2]])

# Fonction pour itérer sur les images de caryotypes
def iter_on_all_caryotypes(path, coord):
    caryotypes_files = os.listdir(path)
    for caryotype in caryotypes_files:
        img = io.imread(os.path.join(path, caryotype), as_gray=True, plugin='pil')
        crop_chromosomes(path, caryotype, img, coord)

# Appel de la fonction pour lancer l'itération sur toutes les images de caryotypes
# iter_on_all_caryotypes("base_donnees/caryotype", data)