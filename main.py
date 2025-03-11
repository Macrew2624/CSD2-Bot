from PIL import Image
import pytesseract
import numpy as np
import pyautogui
import keyboard
import string
import time


def take_recipe_name():
    region = (605, 1230, 750, 75)
    screenshot = pyautogui.screenshot(region=region)
    save_path = r'C:\Users\Tudor Macri\PycharmProjects\CSDBot\image_01.png'
    screenshot.save(save_path)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    filename = 'image_01.png'
    img1 = np.array(Image.open(filename))
    text = pytesseract.image_to_string(img1)
    return text


def pixel_color(i, j):
    region = (i, j, 1, 1)
    screenshot = pyautogui.screenshot(region=region)
    save_path = r'C:\Users\Tudor Macri\PycharmProjects\CSDBot\image_02.png'
    screenshot.save(save_path)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    filename = 'image_02.png'
    img1 = Image.open(filename)
    color = img1.getpixel((0, 0))
    return color


def get_ingredient(i, j, l, w):
    region = (i, j, l, w)
    screenshot = pyautogui.screenshot(region=region)
    save_path = r'C:\Users\Tudor Macri\PycharmProjects\CSDBot\image_03.png'
    screenshot.save(save_path)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    filename = 'image_03.png'
    img1 = np.array(Image.open(filename))
    text = pytesseract.image_to_string(img1, config=r"--psm 6")
    return text


def take_screenshot(i, j, l, w):
    region = (i, j, l, w)
    screenshot = pyautogui.screenshot(region=region)
    save_path = r'C:\Users\Tudor Macri\PycharmProjects\CSDBot\image_04.png'
    screenshot.save(save_path)
    return save_path


def pixel_color_image(i, j, img):
    color = img.getpixel((i, j))
    return color


def get_ingredient_image(i1, i2, j1, j2, img):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    ingredient_text = pytesseract.image_to_string(img[i1:i2, j1:j2], config=r"--psm 6")
    return ingredient_text


def variety_solver(name):
    ingredients = []
    choices = 0
    save_path = take_screenshot(608, 1310, 1405, 60)
    img = Image.open(save_path)
    img_array = np.array(img)
    for i in range(5):
        current_pixel_color = pixel_color_image(260 * i, 0, img)
        if current_pixel_color == (163, 89, 255) or current_pixel_color == (255, 88, 89) or current_pixel_color == (250, 184, 58):
            choices += 1
    print(choices)
    for i in range(choices):
        option = get_ingredient_image(0, 59, 260 * i + 25, 260 * i + 25 + 200 + 100 * int(i == choices - 1), img_array).strip()
        print(option)
        option = option.replace('(', '').replace(')', '').replace('|', '')
        if option[len(option) - 1].isdigit():
            new_ingredient = [option.translate(str.maketrans('', '', string.digits)).strip()] * int(option[len(option) - 1])
        else:
            new_ingredient = [option.translate(str.maketrans('', '', string.digits)).strip()]
        ingredients.extend(new_ingredient)

    print(ingredients)
    parts = 0
    match name:
        case "Custom Cereal Order":
            for i in ingredients:
                if parts == 0:
                    match i:
                        case "M.Wheats":
                            press('m')
                        case "Choc Crisps":
                            press('h')
                        case "Juicy Ooohs":
                            press('j')
                        case "Fiber Blast":
                            press('f')
                        case "Cornflakes":
                            press('c')
                    press('space')
                    parts += 1
                if parts == 1:
                    match i:
                        case "Milk":
                            press('m')
                        case "Strawberries":
                            press('s')
                        case "Bananas":
                            press('b')
                        case "Blueberries":
                            press('l')
            press('enter')

        case "Custom Pepper Order":
            for i in ingredients:
                if parts == 0:
                    match i:
                        case "R.Pepper":
                            press('r')
                        case "G.Pepper":
                            press('g')
                        case "O.Pepper":
                            press('o')
                        case "Y.Pepper":
                            press('y')
                        case "Cut/Hollow":
                            press('c, space')
                            parts += 1
                if parts == 1:
                    match i:
                        case "Spinach":
                            press('s')
                        case "G.Meat":
                            press('m')
                        case "W.Rice":
                            press('r')
                        case "Egg":
                            press('e')
                        case "Couscous":
                            press('o')
                        case "Feta":
                            press('f')
                        case "Cheese":
                            press('c')
                        case "Cilantro":
                            press('l')
            press('enter')

        case "Cut of Steak, Rare" | "Cut of Steak, Blue Rare" | "Cut of Steak, Medium" | "Cut of Steak, Medium Well" | "Cut of Steak, Well Done" | "Cut of Steak, Medium Rare":
            for i in ingredients:
                match i:
                    case "T-Bone":
                        press('t')
                    case "Porterhouse":
                        press('p')
                    case "New York Strip":
                        press('n')
            press('enter')

        case "Custom Baked Wings Order":
            if choices == 1:
                press('w, enter')
            elif choices == 2:
                press('s')
                for i in ingredients:
                    match i:
                        case "S.Asian":
                            press('a')
                        case "Tangy Sauce":
                            press('y')
                        case "Hot Sauce":
                            press('h')
                        case "BBQ Sauce":
                            press('b')
                        case "Extreme Fire":
                            press('e')
                        case "Teriyaki":
                            press('t')
                        case "Parmesan":
                            press('r')
                press('space, w, t, enter')

        case "Custom Trad. Wings Order":
            if choices == 1:
                for i in ingredients:
                    match i:
                        case "BLS.Wings":
                            press('b')
                        case "Trad.Wings":
                            press('t')
                press('d, enter')
            elif choices == 2:
                press('s')
                for i in ingredients:
                    match i:
                        case "S.Asian":
                            press('a')
                        case "Tangy Sauce":
                            press('y')
                        case "Hot Sauce":
                            press('h')
                        case "BBQ Sauce":
                            press('b')
                        case "Extreme Fire":
                            press('e')
                        case "Teriyaki":
                            press('t')
                        case "Parmesan":
                            press('r')
                press('space, w, t, enter')

        case "Shrimp/Tofu Wok Custom Order":
            if choices == 2:
                for i in ingredients:
                    if parts == 0:
                        match i:
                            case "Honey Glaze":
                                press('y')
                            case "Sweet/Sour":
                                press('w')
                            case "Spicy Sau.":
                                press('s')
                            case "Orange Peel":
                                press('r')
                            case "Oil":
                                press('o')
                            case "Ses.Sauce":
                                press('e')
                    if parts == 1:
                        match i:
                            case "Shrimp":
                                press('h')
                            case "Tofu":
                                press('t')
                    parts += 1
            elif choices == 3:
                for i in ingredients:
                    if parts == 0:
                        match i:
                            case "Sweet/Sour":
                                press('w')
                            case "Spicy Sau.":
                                press('s')
                            case "Soy Sauce":
                                press('o')
                            case "Honey Sau.":
                                press('y')
                            case "Sesame Sau.":
                                press('e')
                            case "Broc.Sau.":
                                press('r')
                    if parts == 1:
                        match i:
                            case "Shrimp":
                                press('h')
                            case "Tofu":
                                press('t')
                        press('space')
                    if parts == 2:
                        match i:
                            case "Onions":
                                press('n')
                            case "G.Peppers":
                                press('g')
                            case "Green Beans":
                                press('e')
                            case "Carrots":
                                press('a')
                            case "Broccoli":
                                press('b')
                            case "Celery":
                                press('c')
                            case "Mushrooms":
                                press('m')
                            case "R.Peppers":
                                press('r')
                            case "Scallions":
                                press('space, c')
                            case "Snow Pea":
                                press('space, s')
                            case "Zucchini":
                                press('space, z')
                    parts += 1
            press('enter')

        case "Chicken Wok Custom Order":
            if choices == 2:
                for i in ingredients:
                    if parts == 0:
                        match i:
                            case "Honey Glaze":
                                press('y')
                            case "Sweet/Sour":
                                press('w')
                            case "Spicy Sau.":
                                press('s')
                            case "Orange Peel":
                                press('r')
                            case "Beef Sau.":
                                press('f')
                            case "Ses.Sauce":
                                press('e')
                    if parts == 1:
                        press('k')
                    parts += 1
            elif choices == 3:
                for i in ingredients:
                    if parts == 0:
                        match i:
                            case "Sweet/Sour":
                                press('w')
                            case "Spicy Sau.":
                                press('s')
                            case "Soy Sauce":
                                press('o')
                            case "Honey Sau.":
                                press('y')
                            case "Sesame Sau.":
                                press('e')
                            case "Broc.Sau.":
                                press('r')
                    if parts == 1:
                        press('k, space')
                    if parts == 2:
                        match i:
                            case "Onions":
                                press('n')
                            case "G.Peppers":
                                press('g')
                            case "Green Beans":
                                press('e')
                            case "Carrots":
                                press('a')
                            case "Broccoli":
                                press('b')
                            case "Celery":
                                press('c')
                            case "Mushrooms":
                                press('m')
                            case "R.Peppers":
                                press('r')
                            case "Scallions":
                                press('space, c')
                            case "Snow Pea":
                                press('space, s')
                            case "Zucchini":
                                press('space, z')
                    parts += 1
            press('enter')

        case "Beef/Pork Wok Custom Order":
            if choices == 2:
                for i in ingredients:
                    if parts == 0:
                        match i:
                            case "Honey Glaze":
                                press('y')
                            case "Sweet/Sour":
                                press('w')
                            case "Spicy Sau.":
                                press('s')
                            case "Mongolian":
                                press('m')
                            case "Beef Sau.":
                                press('f')
                            case "Ses.Sauce":
                                press('e')
                    if parts == 1:
                        match i:
                            case "Beef":
                                press('b')
                            case "Pork":
                                press('p')
                    parts += 1
            elif choices == 3:
                for i in ingredients:
                    if parts == 0:
                        match i:
                            case "Sweet/Sour":
                                press('w')
                            case "Spicy Sau.":
                                press('s')
                            case "Soy Sauce":
                                press('o')
                            case "Honey Sau.":
                                press('y')
                            case "Sesame Sau.":
                                press('e')
                            case "Broc.Sau.":
                                press('r')
                    if parts == 1:
                        match i:
                            case "Beef":
                                press('b')
                            case "Pork":
                                press('p')
                        press('space')
                    if parts == 2:
                        match i:
                            case "Onions":
                                press('n')
                            case "G.Peppers":
                                press('g')
                            case "Green Beans":
                                press('e')
                            case "Carrots":
                                press('a')
                            case "Broccoli":
                                press('b')
                            case "Celery":
                                press('c')
                            case "Mushrooms":
                                press('m')
                            case "R.Peppers":
                                press('r')
                            case "Scallions":
                                press('space, c')
                            case "Snow Pea":
                                press('space, s')
                            case "Zucchini":
                                press('space, z')
                    parts += 1
            press('enter')

        case "Custom Shaved Ice Order":
            for i in ingredients:
                if parts == 0:
                    match i:
                        case "B.Sesame":
                            press('b, space')
                        case "Green Tea":
                            press('g, space')
                        case "Mango":
                            press('a, space')
                        case "Red Bean":
                            press('r, space')
                        case "Strawberry":
                            press('s, space')
                        case "Milk":
                            press('m, space')
                        case "Chocolate":
                            press('c, space')
                if parts == 1:
                    match i:
                        case "P.Fruit":
                            press('p, space')
                        case "Straw. Sau.":
                            press('s, space')
                        case "Milk Sauce":
                            press('m, space')
                        case "Choc. Sauce":
                            press('c, space')
                        case "Mango S.":
                            press('a, space')
                if parts == 2:
                    match i:
                        case "Kiwi":
                            press('k')
                        case "Mango":
                            press('m')
                        case "Strawberries":
                            press('s')
                if parts == 3:
                    match i:
                        case "|.Black":
                            press('b')
                        case "Jelly Fig":
                            press('f')
                        case "J. Almond":
                            press('a')
                        case "Boba Pink Pas.":
                            press('p')
                        case "Boba BIk.Bry.":
                            press('e')
                parts += 1
            press('enter')

        case "Custom Ice Cream Scoops":
            for i in ingredients:
                if parts == 0:
                    if i == "Ch. Dip Cone":
                        press('d, space')
                        parts += 1
                    else:
                        press('space')
                        parts += 1
                if parts == 1:
                    match i:
                        case "Vanilla":
                            press('v')
                        case "Chocolate":
                            press('c')
                        case "Mint Choc.":
                            press('m')
                        case "Praline P.":
                            press('p')
                        case "Rocky Road":
                            press('r')
                        case "R.Sherbert":
                            press('s')
                        case "Cookie Dou.":
                            press('d')
                        case "Butter P.":
                            press('b')
            press('enter')

        case "Custom Ice Cream Order":
            for i in ingredients:
                if parts == 0:
                    match i:
                        case "Vanilla":
                            press('v')
                            parts += 1
                            press('space')
                        case "Chocolate":
                            press('c')
                            parts += 1
                            press('space')
                        case "Mint Choc.":
                            press('m')
                            parts += 1
                            press('space')
                        case "Praline P.":
                            press('p')
                            parts += 1
                            press('space')
                        case "Rocky Road":
                            press('r')
                            parts += 1
                            press('space')
                        case "R.Sherbert":
                            press('s')
                            parts += 1
                            press('space')
                        case "Cookie Dou.":
                            press('d')
                            parts += 1
                            press('space')
                        case "Butter P.":
                            press('b')
                            parts += 1
                            press('space')
                if parts == 1:
                    match i:
                        case "Choc.Syr.":
                            press('c')
                            parts += 1
                        case "Straw.Syr.":
                            press('s')
                            parts += 1
                if parts == 2:
                    match i:
                        case "Bananas":
                            press('b')
                            parts += 1
                            press('space')
                        case "Hard Candy":
                            press('h')
                            parts += 1
                            press('space')
                        case "Gummies":
                            press('g')
                            parts += 1
                            press('space')
                        case "Nuts":
                            press('n')
                            parts += 1
                            press('space')
                        case "Sprinkles":
                            press('p')
                            parts += 1
                            press('space')
                        case "Strawberries":
                            press('space')
                            press('s')
                            parts += 1
                        case "Cookie Bits":
                            press('space')
                            press('c')
                            parts += 1
                if parts == 3:
                    match i:
                        case "Whip":
                            press('w')
            press('enter')

        case "Standard Prep (Meat Station)":
            for i in ingredients:
                match i:
                    case "Beef":
                        press('b')
                    case "Chicken":
                        press('k')
                    case "Ground Meat":
                        press('m')
                    case "Shrimp":
                        press('h')
            press('enter')

        case "Standard Prep (Holding Station)":
            try:
                for i in ingredients:
                    match i:
                        case "Artichokes":
                            press('a')
                        case "Asparagus":
                            press('a')
                        case "Bacon":
                            press('b')
                        case "Bean Patty":
                            press('b')
                        case "Beef":
                            press('b')
                        case "Biscuits":
                            press('b')
                        case "Black Beans":
                            press('a')
                        case "Black Rice":
                            press('r')
                        case "Boiled Eggs":
                            press('b')
                        case "Brisket":
                            press('b')
                        case "Broccoli":
                            press('b')
                        case "Brown Rice":
                            press('r')
                        case "Brown Sugar":
                            press('b')
                        case "Butter":
                            press('u')
                        case "B.Sprouts":
                            press('b')
                        case "Cannoli":
                            press('c')
                        case "Carrots":
                            press('a')
                        case "Cauliflower":
                            press('c')
                        case "Celery":
                            press('c')
                        case "Chicken":
                            press('k')
                        case "Chimichanga":
                            press('c')
                        case "Chow Mein":
                            press('h')
                        case "Cilantro":
                            press('c')
                        case "Cooking Oil":
                            press('o')
                        case "Corn Cobs":
                            press('c')
                        case "Croutons":
                            press('r')
                        case "Cucumbers":
                            press('u')
                        case "Donuts":
                            press('o')
                        case "D.Potatoes":
                            press('p')
                        case "Edamame":
                            press('e')
                        case "Eggs":
                            press('e')
                        case "Egg Bits":
                            press('e')
                        case "Fennel":
                            press('f')
                        case "French Toast":
                            press('f')
                        case "Green Bns.":
                            press('g')
                        case "Grits":
                            press('g')
                        case "Ground Meat":
                            press('m')
                        case "Ham":
                            press('h')
                        case "Inject BBQ":
                            press('i')
                        case "Injection":
                            press('i')
                        case "Kale":
                            press('k')
                        case "Lettuce":
                            press('l')
                        case "Lid":
                            press('l')
                        case "Macaroni":
                            press('m')
                        case "Mayo":
                            press('m')
                        case "Meat Patty":
                            press('m')
                        case "Mixed Veg.":
                            press('v')
                        case "Nuggets":
                            press('n')
                        case "O.Shoots":
                            press('s')
                        case "Paprika":
                            press('r')
                        case "Peas":
                            press('p')
                        case "Pinto Beans":
                            press('p')
                        case "Poached Eggs":
                            press('p')
                        case "Potatoes":
                            press('p')
                        case "Prime Rib":
                            press('p')
                        case "Pulled Pork":
                            press('p')
                        case "Raw Chop":
                            press('l')
                        case "Red Cabbage":
                            press('r')
                        case "Ribs":
                            press('r')
                        case "Rice":
                            press('r')
                        case "Roast Beef":
                            press('r')
                        case "Shrimp":
                            press('h')
                        case "Sopapillas":
                            press('s')
                        case "Tomatoes":
                            press('t')
                        case "Tomato Sau.":
                            press('t')
                        case "Turkey":
                            press('u')
                        case "Tuscan Beans":
                            press('b')
                        case "Salt":
                            press('s')
                        case "Sauce":
                            press('a')
                        case "Sauerkraut":
                            press('s')
                        case "Sausages":
                            press('s')
                        case "Sau. Links":
                            press('s')
                        case "Scrambled":
                            press('s + c')
                        case "Seasoning":
                            press('s')
                        case "Soy Sauce":
                            press('s + o')
                        case "Steak Fingers":
                            press('s')
                        case "Strips":
                            press('s')
                        case "Stuffing":
                            press('s')
                        case "Sugar":
                            press('s')
                        case "Sunny Side":
                            press('s')
                        case "Tazukuri":
                            press('t')
                        case "Turkey Leg":
                            press('t')
                        case "Water":
                            press('w')
                        case "White Rice":
                            press('r')
                        case "Wieners":
                            press('w')
                        case "Wild Rice":
                            press('r')
                        case _:
                            press('p + c, k, m, m, m, s')
                            raise ValueError
            except ValueError:
                pass
            if len(ingredients) == 0:
                press('p + c, k, m, m, m, s')
            press('d + l, enter')

        case "Variety Mix (Holding Station)":
            for i in ingredients:
                match i:
                    case "Sweet Po.":
                        press('s')
                    case "Steak Fr.":
                        press('t')
                    case "French Fr.":
                        press('f')
                    case "Shoestring":
                        press('h')
                    case "Curly Fries":
                        press('c')
                    case "Wavy Fries":
                        press('v')
                    case "Waffle Fries":
                        press('w')
                    case _:
                        continue
            press('d, enter')

        case "Seafood Mix":
            for i in ingredients:
                match i:
                    case "Clam":
                        press('l')
                    case "Hushpuppies":
                        press('h')
                    case "Calamari":
                        press('c')
                    case _:
                        continue
            press('d, enter')

        case "Freshly Brewed Iced Tea":
            for i in ingredients:
                match i:
                    case "Classic Tea":
                        press('c')
                    case "Passion Tea":
                        press('p')
                    case "Tropics Tea":
                        press('t')
                    case "Peach Tea":
                        press('e')
                    case "Sweet Tea":
                        press('s')
                    case "Texas Tea":
                        press('x')
            press('b, enter')

        case "Piping Hot Tea":
            for i in ingredients:
                match i:
                    case "Classic Tea":
                        press('c')
                    case "Meditation Tea":
                        press('d')
                    case "Earl Gray Tea":
                        press('e')
                    case "Mint Tea":
                        press('m')
                    case "Chai Tea":
                        press('h')
                    case "Harmony Tea":
                        press('y')
                    case "Haze Tea":
                        press('z')
            press('b, enter')

        case "Freshly Brewed Coffee":
            for i in ingredients:
                match i:
                    case "House Coffee":
                        press('h')
                    case "Decaf Coffee":
                        press('d')
            press('b, enter')

        case "Egg Roll Mix":
            for i in ingredients:
                match i:
                    case "Spr.Rolls":
                        press('s')
                    case "Egg Rolls":
                        press('e')
            press('d, enter')

        case "Fish Mix (Holding Station)":
            for i in ingredients:
                match i:
                    case "Cod":
                        press('c')
                    case "Fish":
                        press('f')
            press('d, enter')

        case "Shrimp Mix (Holding Station)":
            for i in ingredients:
                match i:
                    case "Shrimp":
                        press('h')
                    case "Popcorn Shrimp":
                        press('p')
            press('d, enter')

        case "Red Wine":
            for i in ingredients:
                match i:
                    case "Casu Marzu":
                        press('c')
                    case "Elk":
                        press('e')
                    case "Deckard V.":
                        press('d')
            press('u, enter')

        case "White Wine":
            for i in ingredients:
                match i:
                    case "S.Beard":
                        press('s')
                    case "Eya":
                        press('e')
                    case "Chry 1973":
                        press('c')
            press('u, enter')

        case _:
            print("Invalid recipe")


def solver(name):
    match name:
        case "01. Classic Tacos":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('m, space, s, r, t, space, l, c, g, enter')
            else:
                press('m, o, enter')
        case "02. Beyond the Border":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('m, space, s, r, t, n, space, l, c, o, enter')
            else:
                press('m, o, enter')
        case "03. Crunch Time":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('m, space, q, r, a, space, l, z, g, enter')
            else:
                press('m, o, enter')
        case "04. Nebraska Style":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('m, space, l, r, a, space, l, c, g enter')
            else:
                press('m, o, enter')
        case "05. Juarez Nights":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('m, space, s, r, t, n, space, g, enter')
            else:
                press('m, o, enter')
        case "06. The Loco Taco":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('m, space, z, a, n, space, p, enter')
            else:
                press('m, o, enter')
        case "07. Mexican Delight":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('m, space, l, a, t, space, l, z, p, enter')
            else:
                press('m, o, enter')
        case "08. Spain Fame":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('m, space, q, s, r, t, space, l, u, enter')
            else:
                press('m, o, enter')
        case "09. Chicken Tacos":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('k, space, s, r, t, n, space, l, c, p, enter')
            else:
                press('k, o, enter')
        case "10. The Mexican Chicken":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('k, space, z, a, n, space, p, enter')
            else:
                press('k, o, enter')
        case "11. Feathered Pockets":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('k, space, l, r, t, n, space, l, c, z, g, enter')
            else:
                press('k, o, enter')
        case "12. The Fiesta":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('k, space, s, r, t, space, l, c, u, enter')
            else:
                press('k, o, enter')
        case "13. Beef Supreme":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('b, space, s, r, t, space, l, c, g, enter')
            else:
                press('b, o, enter')
        case "14. The Siesta":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('b, space, s, r, t, n, space, l, c, z, p, enter')
            else:
                press('b, o, enter')
        case "15. Beefy Afternoon":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('b, space, z, r, a space, l, o, enter')
            else:
                press('b, o, enter')
        case "16. Beef Buffs":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('b, space, q, z, r, n, space, r, enter')
            else:
                press('b, o, enter')
        case "17. Pacific Tacos":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('f, space, s, r, t, space, l, c, r, enter')
            else:
                press('f, o, enter')
        case "18. Fish Tacos":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('f, space, s, r, space, l, z, r, enter')
            else:
                press('f, o, enter')
        case "19. Gulf Beachside":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('f, space, z, r, a, t, n, space, o, enter')
            else:
                press('f, o, enter')
        case "20. Fisherman's Taco":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('f, space, z, r, t, n, space, l, c, z, o, enter')
            else:
                press('f, o, enter')

        case "Custom Cereal Order":
            variety_solver(name)

        case "Custom Pepper Order":
            variety_solver(name)

        case "Cut of Steak, Rare" | "Cut of Steak, Blue Rare" | "Cut of Steak, Medium" | "Cut of Steak, Medium Well" | "Cut of Steak, Well Done" | "Cut of Steak, Medium Rare":
            variety_solver(name)

        case "01. Shrimp Press":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('h, r, v, t, space, t, enter')
            else:
                press('p, o, h, enter')
        case "02. Seagreen Delight":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('h, b, m, p, space, s, e, enter')
            else:
                press('p, o, h, enter')
        case "03. Ocean Park":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('h, r, t, m, p, space, t, enter')
            else:
                press('p, o, h, enter')
        case "04. The Spinach Pile":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('r, n, space, s, e, enter')
            else:
                press('p, enter')
        case "05. Healthy Living":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('m, p, space, t, enter')
            else:
                press('p, enter')
        case "06. Verde Light":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('r, n, b, space, e, enter')
            else:
                press('p, enter')

        case "01. Classic Salisbury":
            press('s, g, enter')
        case "02. Mushroom Salisbury":
            press('s, m, enter')
        case "03. Onion Salisbury":
            press('s, o, enter')

        case "Salisbury Steak Prep":
            press('u, s, enter')

        case "01. Classic Ramen Bowl":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('b, m, space, k, m, n, space, s, enter')
            else:
                press('r, o, b, m, enter')
        case "02. Kakuni Spa":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('k, space, u, c, r, k, space, t, enter')
            else:
                press('r, o, k, enter')
        case "03. Elevated Bowl":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('p, space, c, r, e, m, space, t, enter')
            else:
                press('r, o, p, enter')
        case "04. Salty Coast":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('c, m, space, r, e, m, space, c, p, t, enter')
            else:
                press('r, o, c, m, enter')
        case "05. Spicy Bowl":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('s, k, space, c, e, space, c, t, enter')
            else:
                press('r, o, s, k, enter')
        case "06. Nori and Friends":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('p, b, space, u, k, n, space, s, enter')
            else:
                press('r, o, p, b, enter')
        case "07. Sleeper Bowl":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('m, h, space, e, k, m, space, p, enter')
            else:
                press('r, o, m, h, enter')
        case "08. Hot Afternoon":
            if pixel_color(2305, 775) == (130, 44, 44):
                press('c, h, space, r, e, k, space, c, s, enter')
            else:
                press('r, o, c, h, enter')

        case "01. Chicken Quesadilla":
            press('p, k, c, t, enter')
        case "02. Beef Quesadilla":
            press('p, b, c, t, enter')
        case "03. Shrimp Quesadilla":
            press('p, h, c, t, enter')
        case "04. Loaded Quesadilla":
            press('p, b, k, c, t, enter')
        case "05. Spinach Quesadilla":
            press('p, s, c, t, enter')
        case "06. Alamo Quesadilla":
            press('p, s, b, h, c, t, enter')

        case "01. Classic Stack":
            press('p, m, enter')
        case "02. Strawberry Stack":
            press('p, s, enter')
        case "03. Pecan Stack":
            press('p, e, enter')
        case "04. Blueberry Stack":
            press('p, l, enter')

        case "Pancake Prep":
            press('p, p, p, enter')

        case "01. Vanilla Tres Leches":
            press('v, p, m, w, enter')
        case "02. Chocolate Tres Leches":
            press('c, p, c, w, enter')

        case "01. Pulled Pork Sandwich":
            press("p, a, o, enter")
        case "02. P.P. Coleslaw Sandwich":
            press('p, a, c, o, enter')

        case "Standard Prep (Meat Station)":
            variety_solver(name)

        case "01. Classic Nachos":
            press('q, b, space, m, u, enter')
        case "02. South of the Border":
            press('q, t, space, k, s, enter')
        case "03. Beefarita":
            press('q, r, a, space, b, s, enter')
        case "04. Mexican Tornado":
            press('q, v, n, t, space, k, b, enter')
        case "05. Cheesy Hurricane":
            press('q, r, n, t, space, h, s, u, enter')
        case "06. Cheddar Chips":
            press('q, enter')
        case "07. Beantown":
            press('q, b, a, space, k, enter')
        case "08. Meat-a-licious":
            press('q, space, k, h, b, m, enter')
        case "09. Meat-a-licious Supreme":
            press('q, r, v, n, t, space, k, h, b, m, enter')
        case "10. Extreme Fajitas":
            press('q, v, space, k, b, s, u, enter')
        case "11. Infinite Nachos":
            press('q, b, r, v, a, n, t, space, k, h, b, m, s, enter')
        case "12. Queso me Mucho":
            press('q, space, k, b, enter')

        case "01. Beef Chow Mein":
            press('o, h, s, c, b, a, m, space, o, b, enter')
        case "02. Chicken Chow Mein":
            press('o, h, s, c, b, a, m, space, o, k, enter')
        case "03. Shrimp Chow Mein":
            press('o, h, s, c, b, a, m, space, o, h, enter')
        case "04. Pork Chow Mein":
            press('o, h, s, c, b, a, m, space, o, p, enter')
        case "05. Veggie Chow Mein":
            press('o, h, s, c, b, r, a, m, enter')

        case "Biscuits and Gravy":
            press('b, g, enter')

        case "Cinnamon Roll Prep":
            press('c, enter')

        case "Frozen Banana Prep.":
            press('b, n, d, enter')

        case "Blueberry Rote Grutze":
            press('l, d, enter')
        case "Red Currant Rote Grutze":
            press('c, d, enter')
        case "Strawberry Rote Grutze":
            press('s, d, enter')
        case "Blackberry Rote Grutze":
            press('b, d, enter')
        case "Raspberry Rote Grutze":
            press('r, d, enter')

        case "01. Red Enchiladas":
            press('f, c, r, enter')
        case "02. Green Corn Enchiladas":
            press('o, c, g, enter')
        case "03. Queso Mucho Enchiladas":
            press('f, c, q, enter')
        case "04. Queso Mucho Corn Enchiladas":
            press('o, c, q, enter')
        case "05. White Enchiladas":
            press('o, c, w, enter')
        case "06. Green Enchiladas":
            press('f, c, g, enter')

        case "Spaghetti and Meatballs":
            press('s, m, r, enter')

        case "Spaghetti and Meatballs Prep":
            press('s, m, enter')

        case "01. Green Chile Tamales":
            for i in range(6):
                press('h, m, g, w')
            press('enter')
        case "02. Shredded Pork Tamales":
            for i in range(6):
                press('h, m, p, w')
            press('enter')
        case "03. Spicy Chicken Tamales":
            for i in range(6):
                press('h, m, k, w')
            press('enter')
        case "04. Shredded Chkn. Tamales":
            for i in range(6):
                press('h, m, c, w')
            press('enter')
        case "05. Plain Tamales":
            for i in range(6):
                press('h, m, w')
            press('enter')
        case "06. Spicy Pork Tamales":
            for i in range(6):
                press('h, m, r, w')
            press('enter')

        case "01. Tabbouleh Sunrise":
            press('p, space, t, a, g, enter')
        case "02. Tabbouleh Nights":
            press('p, space, n, u, m, enter')
        case "03. Tabbouleh Teak":
            press('c, space, t, a, p, enter')
        case "04. Tabbouleh Fire":
            press('c, space, n, t, g, enter')
        case "05. Tabbouleh Earl":
            press('b, space, u, m, g, enter')
        case "06. Tabbouleh Field":
            press('b, space, n, a, p, enter')

        case "Pig's Blood Cakes":
            press('b, p, c, enter')
        case "Delicious Lamb Chops":
            press('l, a, s, enter')

        case "01. Beef Fried Rice":
            press('r, s, a, p, e, space, o, b, enter')
        case "02. Chicken Fried Rice":
            press('r, s, a, p, e, space, o, k, enter')
        case "03. Shrimp Fried Rice":
            press('r, s, a, p, e, space, o, h, enter')
        case "04. Pork Fried Rice":
            press('r, s, a, p, e, space, o, p, enter')
        case "05. Veggie Fried Rice":
            press('r, s, a, p, e, enter')
        case "06. Deluxe Fried Rice":
            press('r, s, a, p, e, space, o, k, b, enter')
        case "07. Gourmet Fried Rice":
            press('r, s, a, p, e, space, o, h, k, b, p, enter')

        case "01. Roast Beef Classic":
            press('r, b, o, enter')
        case "02. The Beefy Cheesy":
            press('r, q, o, enter')

        case "Prime Rib":
            press('p, s, enter')

        case "Bean Patty Prep":
            press('b, enter')

        # Beer PS, Craft Beer PS
        case "Beer Pitcher":
            keyboard.press('p')
            time.sleep(1.3)
            keyboard.release('p')
            press('enter')

        # Cannoli PS
        case "Cannoli Prep":
            press('c, d, enter')

        # Chicken Nuggets PS
        case "01. Chicken Nugget Basket":
            press('n, d, enter')

        case "Chicken Prep":
            press('k, enter')

        # Chicken Strips PS
        case "01. Chicken Strip Basket":
            press('s, d, enter')

        # Chimichanga PS
        case "Chimichanga Prep":
            press('c, d, enter')

        # Ice Cream Scoops PS #1
        case "Cone Prep":
            press('w, l, enter')

        # Croissant SD
        case "Croissant Prep":
            press('c, enter')

        # Ribs HS, Ribs PS
        case "Delicious Ribs":
            press("r, a, s, enter")

        case "Delicious Sopapillas":
            press("p, h, s, d, enter")

        # Eggplant Parmigiana PS #1, Eggplant Parmigiana #2
        case "Eggplant Parmesan":
            press('o, e, t, p, r, enter')

        # Side Egg Drop Soup SD
        case "Egg Drop Soup":
            press('e, c, m, enter')

        # Fire Emergency Chore
        case "Emergency (FIRE)":
            keyboard.press('e')
            time.sleep(4)
            keyboard.release('e')
            press('enter')

        # Juice Bar PS
        case "Fresh Juices":
            press('l, m, r, c, o, a, enter')

        # Fresh Lemonade PS
        case "Fresh Lemonade":
            press("c, l, enter")

        # Pineapple Juice PS
        case "Fresh Pineapple Juice":
            press('c, p, enter')

        # Fried Okra SD
        case "Fried Okra (Holding Station)":
            for i in range(4):
                press('o')
            press('d, enter')

        # Funnel Cake PS #1
        case "Funnel Cake Prep":
            press('b, d, enter')

        # Hash Browns SD
        case "Hash Browns (Holding Station)":
            for i in range(4):
                press('h')
            press('d, enter')

        # Horchata PS
        case "Horchata":
            press('c, h, enter')

        # Hotdog PS #1
        case "Hotdog Prep":
            press("w, enter")

        case "Huge Turkey Leg":
            press('t, enter')

        # Soda Fountain PS
        case "Ice Refill":
            press('o, i, s, enter')

        # Marshmallow Squares SD
        case "Marshmallow Squares Prep":
            press('w, c, m, enter')

        case "Oatmeal Prep":
            press('o, enter')

        # Onigiri SD
        case "Onigiri Mix (Holding Station)":
            press('r, i, s, h, n, enter')

        # Onion Rings SD
        case "Onion Rings (Holding Station)":
            for i in range(4):
                press('n')
            press('d, enter')

        # Pakora SD
        case "Pakoras (Holding Station)":
            for i in range(4):
                press('p')
            press('d, enter')

        # Oatmeal SD
        case "Side Oatmeal Prep":
            press('o, enter')

        # Steak Fingers PS
        case "Steak Finger Basket":
            press('s, d, enter')

        # Tater Tots SD
        case "Tater Tots (Holding Station)":
            for i in range(4):
                press('t')
            press('d, enter')

        # Dishes Chore
        case "Work Ticket (Dishes)":
            press('d, w')
            time.sleep(2.5)
            press('r, u, s, enter')

        # Pests Chore
        case "Work Ticket (Pests)":
            press('t, c, s, enter')

        # Rat Traps Chore
        case "Work Ticket (Rat Traps)":
            press('l, c, s, enter')

        # Restroom Chore
        case "Work Ticket (Restroom)":
            press('f, s, enter')

        # Roach Traps Chore
        case "Work Ticket (Roach Traps)":
            press('t, s, enter')

        # Trash Chore
        case "Work Ticket (Trash)":
            press('t')
            for i in range(10):
                press('m')
            press('s, enter')

        case "Yaki Tomorokoshi":
            for i in range(4):
                press('c')
            press('s, u, enter')

        case "Beef/Pork Wok Custom Order":
            variety_solver(name)

        case "Chicken Wok Custom Order":
            variety_solver(name)

        case "Custom Baked Wings Order":
            variety_solver(name)

        # Ice Cream Sundae PS
        case "Custom Ice Cream Order":
            variety_solver(name)

        # Ice Cream Scoops PS #2
        case "Custom Ice Cream Scoops":
            variety_solver(name)

        # Taiwanese Shaved Ice PS
        case "Custom Shaved Ice Order":
            variety_solver(name)

        case "Custom Trad. Wings Order":
            variety_solver(name)

        # Egg Rolls SD
        case "Egg Roll Mix":
            variety_solver(name)

        case "Fish Mix (Holding Station)":
            variety_solver(name)

        case "Freshly Brewed Coffee":
            variety_solver(name)

        case "Freshly Brewed Iced Tea":
            variety_solver(name)

        case "Piping Hot Tea":
            variety_solver(name)

        case "Red Wine":
            variety_solver(name)

        case "Seafood Mix":
            variety_solver(name)

        case "Shrimp/Tofu Wok Custom Order":
            variety_solver(name)

        case "Shrimp Mix (Holding Station)":
            variety_solver(name)

        # Asparagus SD, Bacon SD, Baked Potato SD, Black Beans SD, Broccoli SD, Brussels Sprouts SD, Side Chow Mein SD, Corn on the Cob SD
        # Sauerkraut SD, Edamame SD, German Red Cabbage SD, Green Beans SD
        case "Standard Prep (Holding Station)":
            variety_solver(name)

        # Fries SD
        case "Variety Mix (Holding Station)":
            variety_solver(name)

        case "01. Chopped Brisket Sandwich":
            press('r, b, o, enter')
        case "02. Spicy Brisket Sandwich":
            press('r, s, o, enter')

        case "01. Sunny Side Up":
            press('s, enter')
        case "02. Scrambled Eggs":
            press('c, enter')

        case "01. White Toasted Bread":
            press('w, enter')
        case "02. Wheat Toasted Bread":
            press('h, enter')

        case "01. Classic Cod Basket":
            press('c, d, enter')
        case "02. Classic Fish Basket":
            press('f, d, enter')

        case "01. Classic Shrimp Basket":
            press('h, d, enter')
        case "02. Classic Pop. Shrimp Basket":
            press('p, d, enter')

        # Dinner Roll SD
        case "01. White Bread Rolls":
            press('w, enter')
        case "02. Wheat Bread Rolls":
            press('h, enter')

        case "Classic Pretzels (Holding Station)":
            press('c, enter')
        case "German Pretzels (Holding Station)":
            press('g, enter')

        case "01. Classic Meatloaf":
            press('m, a, enter')
        case "02. Bacon Wrapped Meatloaf":
            press('m, a, b, enter')

        case "01. Cinnamon Oatmeal":
            press('c, enter')
        case "02. Cranberry Oatmeal":
            press('c, r, enter')
        case "03. Almond Oatmeal":
            press('c, a, enter')

        # Fruit Spread SD
        case "01. Spring Mix (Holding Station)":
            press('c, t, s, k, enter')
        case "02. Summer Mix (Holding Station)":
            press('g, c, a, t, enter')
        case "03. Beach Mix (Holding Station)":
            press("g, a, s, k, enter")

        case "01. Classic Funnel Cake":
            press('w, p, c, enter')
        case "02. Chocolate Funnel Cake":
            press('w, c, enter')
        case "03. White Funnel Cake":
            press('w, p, enter')

        case "01. Corn Chip Classic":
            press('h, c, j, enter')
        case "02. Oklahoma Pie":
            press('h, c, j, n, enter')
        case "03. Freedom Pie":
            press('c, j, n, enter')

        case "01. Chicken Breast":
            press('c')
            for i in range(6):
                press('t')
            press('s, enter')
        case "01. Winner's Dinner":
            press('c')
            for i in range(6):
                press('t')
            press('s, enter')
        case "02. Breaded Chicken Breast":
            press('c')
            for i in range(6):
                press('t')
            press('b, enter')

        case "01. Swamp Stew":
            press('o, b, e, a, enter')
        case "02. Rusty Bolts":
            press('o, b, p, n, enter')
        case "03. Savannah Glaze":
            press('o, b, p, e, enter')
        case "04. Alabama Glass":
            press('o, b, e, a, n, enter')

        case "01. Alabama Sunrise":
            press('r, t, h, e, c, o, n, enter')
        case "02. Southern Secret":
            press('r, t, n, space, o, s, enter')
        case "03. New Orleans Hangover":
            press('r, h, o, n, space, o, s, enter')
        case "04. FlavorGator":
            press('r, h, e, space, o, s, enter')

        case "01. Destination Maine":
            press('h, b, f, c, l, p, enter')
        case "02. Charleston Chowder":
            press('h, c, a, p, space, o, p, enter')
        case "03. Midnight Harbor":
            press('f, a, l, space, o, k, enter')
        case "04. Silver Reef":
            press('b, f, c, a, l, space, o, p, enter')

        case "01. Grand Slam Nachos":
            press('q, s, j, enter')
        case "02. Touchdown Nachos":
            press('q, j, b, enter')
        case "03. Slam Dunk Nachos":
            press('q, s, j, b, enter')
        case "04. Hole In One Nachos":
            press('q, s, b, enter')

        case "01. The Gerstmann":
            press('k, enter')
        case "01. Red Dog":
            press('k, enter')
        case "02. Yellow Dog":
            press('m, enter')
        case "03. Deluxe Dog":
            press("k, m, enter")
        case "04. Dry Dog":
            press('enter')

        case "01. Texas Chili Bowl":
            press('o, m, b, g, n, enter')
        case "02. Chunky Fire Chili":
            press('o, m, g, r, enter')
        case "03. Sunshine Road":
            press('o, m, g, r, n, enter')
        case "04. Rock n' Roll Bowl":
            press('o, m, b, r, t, enter')

        case "01. The Classic Lasagna":
            press('p, s, c, r, p, s, c, r, p, s, c, enter')
        case "02. Meaty Rome Lasagna":
            press('p, s, m, c, r, p, s, c, r, p, s, c, enter')
        case "03. Veggie Lasagna":
            press('p, s, v, c, r, p, s, c, r, p, s, c, enter')
        case "04. Spinach Lasagna":
            press('p, s, n, c, r, p, s, c, r, p, s, c, enter')

        case "01. Grilled Chicken Classic":
            press('k, s, p, o, enter')
        case "02. Grilled Chicken Deluxe":
            press('k, t, l, p, o, enter')
        case "03. Loaded Chicken Griller":
            press('k, t, l, b, s, o, enter')
        case "04. Swiss Chicken Burger":
            press('k, t, b, s, o, enter')

        case "01. Blueberry Muffins":
            press('n, l, enter')
        case "02. Bran Muffins":
            press('n, b, enter')
        case "03. Chocolate Muffins":
            press('n, o, enter')
        case "04. Cranberry Muffins":
            press('n, c, enter')
        case "05. Banana Muffins":
            press('n, a, enter')

        case "01. Chocolate Chip Batch":
            press('c, enter')
        case "02. Dark Chocolate Batch":
            press('d, enter')
        case "03. Candy Cookie Batch":
            press('a, enter')
        case "04. Peanut Butter Batch":
            press('p, enter')
        case "05. Oatmeal Batch":
            press('o, enter')
        case "06. Sugar Batch":
            press('s, enter')

        case "01. Classic Bean":
            press('b, t, l, o, enter')
        case "02. Bean Surpreme":
            press('b, t, p, n, l, o, enter')
        case "03. Avocado Fresh":
            press('b, v, l, o, enter')
        case "04. Hawaiian Memories":
            press('b, p, i, l, o, enter')
        case "05. Veggie Bean Blast":
            press('b, t, p, v, o, enter')
        case "06. Beanie":
            press('b, i, v, o, enter')

        case "01. MK Teleport Punch":
            press('a, b, r, c, enter')
        case "02. Spinning Bird Kick":
            press('b, y, l, d, enter')
        case "03. Phoenix Bone Breaker":
            press('a, x, l, d, enter')
        case "04. Hwang's Blazing Thrust":
            press('b, x, y, r, enter')
        case "05. Resshou Rasengeki":
            press('b, x, l, c, enter')
        case "06. Flying Elbow Drop":
            press('x, l, r, d, enter')

        case "01. Broccoli Deluxe Soup":
            press('r, c, e, space, b, enter')
        case "02. Classic Lentil":
            press('b, c, a, l, enter')
        case "03. Tortilla Soup":
            press('t, n, space, t, enter')
        case "04. Potato and Chicken":
            press('b, c, e, space, o, k, p, enter')
        case "05. Veggie Soup":
            press('b, c, a, e, space, m, p, enter')
        case "06. Chicken Noodle Classic":
            press('b, n, space, o, k, enter')

        case "01. Sausage and Cheese":
            press('s, c, i, enter')
        case "02. Egg and Ham":
            press('h, e, i, enter')
        case "03. Egg Deluxe":
            press('e, b, c, i, enter')
        case "04. Sausage, Egg and Cheese":
            press('s, e, c, i, enter')
        case "05. French Ham":
            press('h, e, r, enter')
        case "06. French Cheesy":
            press('s, c, r, enter')

        case "01. Double Mocha Cheesecake":
            press('m, m, c, enter')
        case "02. Tiramisu Creme":
            press('t, t, b, enter')
        case "03. Banapple":
            press('a, b, b, enter')
        case "04. Dark Creamy Goodness":
            press('m, m, b, enter')
        case "05. Chocolate Key Lime":
            press('m, m, k, enter')
        case "06. The Chicago Sampler":
            press('c, b, k, enter')
        case "07. Mexican Paradise":
            press('m, a, t, enter')
        case "08. The San Francisco Sampler":
            press('t, b, k, enter')
        case "09. Dark Mess":
            press('m, m, m, enter')
        case "10. Triple Shot":
            press('b, b, b, enter')

        case "01. Vanilla Paradise":
            press('c, v, space, c, o, s, enter')
        case "02. Vanilla Tang":
            press('c, v, n, enter')
        case "03. Vanilla Holiday":
            press('c, v, g, space, a, s, enter')
        case "04. Vanillache":
            press('c, v, space, h, o, s, enter')
        case "05. Chocolot":
            press('c, h, s, space, a, s, enter')
        case "06. Chocrazy":
            press('c, h, space, h, o, s, enter')
        case "07. Mud":
            press('c, h, n, space, a, s, enter')
        case "08. Chocnrock":
            press('c, h, space, m, o, s, enter')
        case "09. Pink Fruit":
            press('c, p, o, space, a, s, enter')
        case "10. Pink Splendor":
            press('c, p, space, c, o, s, enter')
        case "11. Pink Passion":
            press('c, p, g, space, a, s, enter')
        case "12. Pinklectric":
            press('c, p, space, p, o, s, enter')

        case "01. California Roll":
            press('r, e, v, s, space, y, space, r, r')
            for i in range(9):
                press('c')
            press('enter')
        case "02. Spider Roll":
            press('r, e, v, space, y, f, space, r, r')
            for i in range(9):
                press('c')
            press('enter')
        case "03. Ocean Roll":
            press('r, u, a, c, space, w, n, space, r, r')
            for i in range(9):
                press('c')
            press('enter')
        case "04. Firecracker Roll":
            press('r, e, h, space, w, a, space, r, r')
            for i in range(9):
                press('c')
            press('enter')
        case "05. Drum Roll":
            press('r, a, h, space, a, n, space, r, r')
            for i in range(9):
                press('c')
            press('enter')
        case "06. Osaka Roll":
            press('r, u, h, space, y, e, space, r, r')
            for i in range(9):
                press('c')
            press('enter')
        case "07. Salty Roll":
            press('r, a, c, h, space, y, a, space, r, r')
            for i in range(9):
                press('c')
            press('enter')
        case "08. Gated Roll":
            press('r, e, u, c, space, w, e, space, r, r')
            for i in range(9):
                press('c')
            press('enter')
        case "09. Slaughter Roll":
            press('r, s, c, space, w, e, n, space, r, r')
            for i in range(9):
                press('c')
            press('enter')
        case "10. Splatter Roll":
            press('r, e, a, space, y, w, a, space, r, r')
            for i in range(9):
                press('c')
            press('enter')
        case "11. Champ Roll":
            press('r, u, s, c, space, f, space, r, r')
            for i in range(9):
                press('c')
            press('enter')
        case "12. Jammy Roll":
            press('r, s, space, y, a, f, space, r, r')
            for i in range(9):
                press('c')
            press('enter')

        case "01. Classic Dog":
            press('r, space, c, r, m, enter')
        case "02. Westminster Dog":
            press("r, space, c, r, k, enter")
        case "03. Chili Dog":
            press("r, space, c, h, n, m, enter")
        case "04. Texas Dog":
            press("r, space, c, h, enter")
        case "05. Rawdawg":
            press("z, space, m, enter")
        case "06. Twisted Dog":
            press("z, space, c, k, enter")
        case "07. Salty Dog":
            press("z, space, n, m, k, enter")
        case "08. Green Dog":
            press('z, space, r, enter')
        case "09. Cheesey Dog":
            press("p, space, c, enter")
        case "10. Fog Dog":
            press("p, space, n, m, k, enter")
        case "11. Dang Dog":
            press("p, enter")
        case "12. Plop Dog":
            press('p, space, c, r, h, n, m, k, enter')

        case "O1. Crisp Texas Greens":
            press('r, space, b, c, e, r, t, space, n, enter')
        case "02. Caesar Salad":
            press('c, space, p, r, space, g, enter')
        case "03. Creamy Ranch":
            press('r, space, e, r, m, t, space, u, enter')
        case "04. Grilled Chicken Salad":
            press('r, space, c, e, r, m, t, space, g, enter')
        case "05. Crispy Chicken Salad":
            press('r, space, c, e, r, m, t, space, f, enter')
        case "06. Thousand Island Special":
            press('t, space, c, r, m, space, b, n, enter')
        case "07. Chopped Pink Salad":
            press('t, space, b, p, r, space, h, enter')
        case "08. Garden Salad":
            press('t, space, c, r, t, enter')
        case "09. Parm Salad Special":
            press('c, space, p, r, space, b, u, enter')
        case "10. Simple Salad":
            press('r, space, c, r, enter')
        case "11. House Salad":
            press('r, space, b, c, r, space, n, enter')
        case "12. Velvet Salad":
            press('v, space, r, m, t, space, b, n, enter')
        case "13. The Big Salad":
            press('v, space, b, e, r, t, space, g, n, enter')
        case "14. Veggie Life":
            press('v, space, e, r, m, t, space, b, n, u, enter')

        case "01. Apple Pie":
            press('c, a, space, space, l, enter')
        case "02. Banana Creme Pie":
            press('g, b, space, space, w, enter')
        case "03. Chocolate Creme Pie":
            press('g, h, space, space, w, enter')
        case "04. Key Lime Pie":
            press('c, k, enter')
        case "05. Lemon Meringue Pie":
            press('g, l, space, space, w, enter')
        case "06. Millionaire Pie":
            press('g, m, space, space, w, enter')
        case "07. Blueberry Pie":
            press('c, space, b, space, l, enter')
        case "08. Cherry Pie":
            press('c, space, c, space, v, enter')
        case "09. Coconut Meringue Pie":
            press('g, space, o, space, o, enter')
        case "10. Mincemeat Pie":
            press('c, space, m, space, v, enter')
        case "11. Peach Pie":
            press('c, space, p, space, v, enter')
        case "12. Pumpkin Pie":
            press('c, space, u, enter')
        case "13. Rhubarb Pie":
            press('c, space, r, space, w, enter')
        case "14. Strawberry Pie":
            press('c, space, s, space, l, enter')
        case "15. Cranberry Pie":
            press('g, space, space, c, w, enter')
        case "16. Pecan Pie":
            press('c, space, space, p, enter')

        case "01. Classic American":
            press('m, b, l, t, space, r, enter')
        case "02. The Ryan Davis":
            press('m, b, c, c, t, space, r, enter')
        case "03. Fresh Stack":
            press('m, l, t, n, space, r, enter')
        case "04. International Burger":
            press('m, b, s, p, space, m, r, enter')
        case "05. The Mechanic":
            press('m, b, c, l, n, space, z, enter')
        case "06. The Lauren Hiigelburger":
            press('m, b, c, s, space, z, enter')
        case "07. Twisty Cow":
            press('m, b, c, space, n, z, enter')
        case "08. Summer Hay":
            press('m, n, space, m, e, r, enter')
        case "09. Bacon Cheeseburger":
            press('m, b, c, c, l, space, r, enter')
        case "10. Prime Burger":
            press('m, b, n, space, e, r, enter')
        case "11. The Double":
            press('m, m, c, space, r, enter')
        case "12. The Lumberjack":
            press('m, m, b, c, s, space, n, z, enter')
        case "13. Dr.Feelgood":
            press('m, m, b, c, space, r, enter')
        case "14. Parallel Patties":
            press('m, m, space, r, enter')
        case "15. Burger Time":
            press('m, m, l, t, p, space, e, r, enter')
        case "16. The Heartstopper":
            press('m, m, b, c, c, s, space, r, enter')
        case "17. Triple Tower":
            press('m, m, m, b, c, c, n, space, n, m, r, enter')
        case "18. Stacked Panic":
            press('m, m, m, b, l, s, space, e, z, enter')
        case "19. The Beltsmasher":
            press('m, m, m, b, c, c, s, space, r, enter')
        case "20. The Destroyer":
            press('m, m, m, b, c, c, l, t, s, n, space, m, r, enter')

        case "01. Classic Pepperoni":
            press('h, r, c, space, p, enter')
        case "02. Meat Lovers":
            press('s, r, c, space, p, s, g, b, enter')
        case "03. Veggie Tomato":
            press('t, r, c, space, space, m, v, s, g, r, enter')
        case "04. Ham and Pineapple":
            press('h, r, c, space, h, space, i, enter')
        case "05. Supreme":
            press('h, r, c, space, g, space, m, n, v, g, t, enter')
        case "06. Beefy Tomato":
            press('h, r, c, space, s, g, r, space, r, t, enter')
        case "07. Pesto Pepperoni":
            press('h, e, c, space, p, enter')
        case "08. Pesto and Anchovies":
            press('h, e, c, space, a, space, m, n, g, enter')
        case "09. Green Gardens":
            press('t, e, c, space, r, space, v, s, g, enter')
        case "10. Meat-esto":
            press('s, e, c, space, p, s, b, space, g, r, enter')
        case "11. New Jersey Classic":
            press('s, e, c, space, r, a, b, space, n, i, enter')
        case "12. Light and Crisp":
            press('t, e, c, space, k, space, m, enter')
        case "13. White Desert":
            press('h, a, c, space, p, b, enter')
        case "14. Italian Tour":
            press('s, a, c, space, g, r, k, space, v, g, r, enter')
        case "15. Creamy Pie":
            press('s, a, c, space, r, enter')
        case "16. Meaty Alfredo":
            press('h, a, c, space, p, g, k, enter')
        case "17. Mega Queso":
            press('s, q, c, space, s, r, space, n, s, t, enter')
        case "18. Meaty Queso":
            press('h, q, c, space, p, g, k, b, enter')
        case "19. DeLight Queso":
            press('t, q, c, space, space, m, v, s, r, enter')
        case "20. Ham and Cheese":
            press('h, q, c, space, h, r, enter')

        case _:
            print("Invalid recipe")


def press(key):
    key_presses = key.strip().split(', ')
    for i in range(len(key_presses)):
        print(key_presses[i])
        keyboard.press(key_presses[i])
        time.sleep(0.05)
        keyboard.release(key_presses[i])
        time.sleep(0.03)


def calculate_hs_number():
    number_of_hs = 0
    for i in range(502, 502 + 163 * 8, 163):
        print(pixel_color(i, 0))
        if pixel_color(i, 0) == (81, 81, 81):
            number_of_hs += 1
    return number_of_hs


def calculate_ps_number():
    number_of_ps = 0
    for i in range(151, 151 + 98 * 14, 98):
        if pixel_color(0, i) == (158, 158, 158):
                number_of_ps += 1
    return number_of_ps


def calculate_hs_foods():
    counter = 0
    for i in range(2155, 2155 + 205 * 2, 205):
        for j in range(310, 310 + 133 * 4, 133):
            if pixel_color(i, j) == (255, 255, 255):
                counter += 1
    return counter


def run():
    number_of_hs = calculate_hs_number()
    number_of_ps = calculate_ps_number()

    press('tab+1')
    number_of_hs_required = calculate_hs_foods()
    press('space')
    number_of_hs_optional = calculate_hs_foods()
    press('space')
    number_of_side_dishes = calculate_hs_foods()
    press('enter')
    min_number_of_hs = min(number_of_hs, number_of_hs_required + number_of_hs_optional + number_of_side_dishes)
    number_of_hs_in_use = number_of_hs

    print(number_of_hs, number_of_hs_required, number_of_hs_optional, number_of_side_dishes, number_of_hs_in_use, number_of_ps)

    holding_stations = [0] * number_of_hs_in_use
    prep_stations = [0] * number_of_ps

    hs_commands = []

    default_letter = 'a'
    if min_number_of_hs != 0:
        while len(hs_commands) < number_of_hs_in_use:
            for i in range(number_of_hs_required):
                command = 'tab+' + str(1 + len(hs_commands)) + ', ' + chr(ord(default_letter) + i)
                hs_commands.append(command)
            for i in range(number_of_hs_optional):
                command = 'tab+' + str(1 + len(hs_commands)) + ', ' + 'space, ' + chr(ord(default_letter) + i)
                hs_commands.append(command)
            for i in range(number_of_side_dishes):
                command = 'tab+' + str(1 + len(hs_commands)) + ', ' + 'space, space, ' + chr(ord(default_letter) + i)
                hs_commands.append(command)
    else:
        number_of_hs_in_use = 0

    print(hs_commands)
    current_ps = 0
    while True:
        while True:
            if pixel_color(33 + 7 * (current_ps // 10), 170 + 98 * current_ps) == (255, 255, 255):
                if pixel_color(395, 208 + 98 * current_ps) == (78, 50, 137) or pixel_color(410, 201 + 98 * current_ps) == (207, 193, 237):
                    prep_stations[current_ps] = 1
                elif pixel_color(389, 208 + 98 * current_ps) == (0, 216, 255):
                    prep_stations[current_ps] = 0
                if prep_stations[current_ps] == 0 and pixel_color(389, 208 + 98 * current_ps) != (255, 255, 0) and pixel_color(389, 208 + 98 * current_ps) != (255, 28, 0):
                    if current_ps < 9:
                        press(str(current_ps + 1).strip())
                    elif current_ps == 9:
                        press('0')
                    elif current_ps == 10:
                        press('_')
                    elif current_ps == 11:
                        press('=')
                    elif current_ps == 12:
                        press('[')
                    elif current_ps == 13:
                        press(']')
                    recipe_name = take_recipe_name().strip()
                    print('Recipe Name:', recipe_name)
                    if recipe_name != "":
                        solver(recipe_name)
            current_ps += 1
            if current_ps == number_of_ps:
                current_ps = 0
                for i in range(number_of_hs_in_use):
                    if pixel_color(520 + 163 * i, 65) == (103, 103, 103) and holding_stations[i] == 1:
                        holding_stations[i] = 0
                    elif pixel_color(570 + 163 * i, 110) == (130, 130, 130):
                        press("tab+" + str(i + 1))
                        holding_stations[i] = 0
                # for i in range(455, 455 + 162 * number_of_hs_in_use, 162):
                #     if pixel_color(i, 24) == (108, 108, 108) and holding_stations[(i - 455) // 162] == 1:
                #         holding_stations[(i - 455) // 162] = 0
                #     elif pixel_color(i + 114, 137) == (130, 130, 130):
                #         press("tab+" + str((i - 455) // 162 + 1))
                #         holding_stations[(i - 455) // 162] = 0
                for i in range(number_of_hs_in_use):
                    if holding_stations[i] == 0:
                        press(hs_commands[i].strip())
                        recipe_name = take_recipe_name().strip()
                        solver(recipe_name)
                        holding_stations[i] = 1


run()
