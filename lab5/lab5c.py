import lab5b

def test_pixel_constraint():
    """Tests different normal- and edge cases (pixels) and checks whether expected results are recieved"""
    pixel1 = (0, 0, 0)
    pixel2 = (128, 128, 128)
    pixel3 = (50, 100, 200)
    pixel4 = (255, 255, 255)
    pixel5 = (150, 200, 200)
    pixel6 = ("150", 200, 200)
    pixel7 = ((150, 200), 200)


    test_result = lab5b.pixel_constraint(50, 200, 100, 150, 100, 255)

    result1 = test_result(pixel1)
    result2 = test_result(pixel2)
    result3 = test_result(pixel3)
    result4 = test_result(pixel4)
    result5 = test_result(pixel5)

    try:
        test_result(pixel6)
    except TypeError:
        raise TypeError("Index must be an integer")
    
    try:
        test_result(pixel7)
    except TypeError:
        raise TypeError("Index must be an integer")

    assert(result1 == 0)
    assert(result2 == 1)
    assert(result3 == 1)
    assert(result4 == 0)
    assert(result5 == 0)

    print("The code has passed all the tests.")

#test_pixel_constraint()

def test_generator_from_image():
    """Tests generator_from_image too see if expected results are recieved"""
    lst = [(50, 50, 100),(150,50,200),(200,200,50)]

    generator_result = lab5b.generator_from_image(lst)

    for i in range(len(lst)):
        test_result = generator_result(i)
        assert(test_result == lst[i])

    print("The code has passed all the tests.")

#test_generator_from_image()

def test_combine_images():
    """Tests if comebine_images returns expected results"""
    bgr_list = [(0,0,0), (128,128,128), (255,255,255)]
    condition = lab5b.gradient_condition

    lst_image1 = [(255,255,255),(128,128,128),(0,0,0)]
    lst_image2 = [(0,0,0),(128,128,128),(255,255,255)]
    
    generator1 = lab5b.generator_from_image(lst_image1)
    generator2 = lab5b.generator_from_image(lst_image2)

    test_result = lab5b.combine_images(bgr_list,condition,generator1,generator2)
    assert(test_result == [(255,255,255),(128,128,128),(255,255,255)])

    print("The code has passed all the tests.")

#test_combine_images()
