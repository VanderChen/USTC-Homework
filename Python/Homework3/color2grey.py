from graphics import *

def rgb2grey(input_file_path,output_file_path):
    # Get image size
    input_file = Image(Point(0,0), input_file_path)
    width = input_file.getWidth()
    height = input_file.getHeight()

    # Caculate center point
    centerWidth = width / 2
    centerHeight = height / 2
    centerPoint = Point(centerWidth, centerHeight)

    # Get center
    image = Image(centerPoint, input_file_path)
    win = GraphWin("Grayscale", width, height)
    image.draw(win)

    # Draw the grayscale image
    pt = win.getMouse()
    if pt:
        for x in range(width):
            for y in range(height):
                r, g, b = image.getPixel(x, y)
                gray = int(round(0.299 * r + 0.587 * g + 0.114 * b))
                image.setPixel(x,y, color_rgb(gray, gray, gray))
                win.update()

    # save image and clean
    image.save(output_file_path)
    win.getMouse()
    win.close()
    pass

def main():
    input_file_path = input("Please input the input file path of the image:")
    output_file_path = input("Please input the output file path of the image:")

    # Check file exists
    if os.path.exists(input_file_path):
        rgb2grey(input_file_path,output_file_path)
    else:
        main()

if __name__ == '__main__':
    main()