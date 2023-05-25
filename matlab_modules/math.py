import matlab.engine



class Math:
    def __init__(self):
        self.eng = matlab.engine.start_matlab()

    def resize(self, img_path: str):
        RGB = self.eng.imread(img_path)
        h, w, dim = self.eng.size(RGB, nargout=3)
        I = self.eng.im2gray(RGB, nargout=1)
        xtop = float(w / 2)
        ytop = 0.0
        xleft = 0.0
        yleft = float(h / 2)
        xright = float(w)
        yright = float(h / 2)
        xbot = float(w / 2)
        ybot = float(h)
        P = self.eng.impixel(I, 1000.0, 200.0, nargout=1)
        while True:
            P = self.eng.impixel(I, xtop, ytop, nargout=1)
            if P[0][0] > 0.0:
                break
            ytop = ytop + 1
        while True:
            P = self.eng.impixel(I, xleft, yleft)
            if P[0][0] > 0.0:
                break
            xleft = xleft + 1
        while True:
            P = self.eng.impixel(I, xright, yright)
            if P[0][0] > 0.0:
                break
            xright = xright - 1
        while True:
            P = self.eng.impixel(I, xbot, ybot)
            if P[0][0] > 0.0:
                break
            ybot = ybot - 1

        I2 = self.eng.imcrop(I,  self.eng.cell2mat([float(xleft), float(ytop), float(xright - xleft), float(ybot - ytop)]), nargout=1)
        [h2, w2, dim] = self.eng.size(I2, nargout=3)
        I3 = self.eng.insertShape(
            I2, 'filled-rectangle', self.eng.cell2mat([0.0, 0.0, 0.08 * w2, 0.4 * h2]
                                                      ), 'Color', {'black'}, 'Opacity', 1)
        # x = [0, 0.08 * w2, 0.08 * w2, 0]
        # y = [0, 0, 0.4 * h2, 0.4 * h2]
        # J = self.eng.roipoly(I2, self.eng.cell2mat([float(xleft), float(xright), float(xright), float(xleft)]),
        #                      self.eng.cell2mat([float(ytop), float(ytop), float(ybot), float(ybot)]), nargout=1)


        [h, w] = self.eng.size(I3, nargout=2)

        left_side = I3[1:int(h)][1:int(w/2)]
        right_side = I3[1:int(h)][int(w/2):int(w)]
        output = self.eng.uint8(left_side)
        outputF = self.eng.uint8(self.eng.zeros(h, w))
        Pred = round(h * 2 / 16)
        St = 1
        Fin = Pred
        Mo = self.eng.graythresh(output[St:Fin][:])
        Up_image1 = self.eng.im2bw(output[St:Fin][:], Mo)
        outputF[int(St): int(Fin)][1: int(w / 2)] = self.eng.double(Up_image1)
        self.eng.figure, self.eng.imshow(outputF), self.eng.title('IMAGE')
        self.exit_engine()

    def exit_engine(self):
        self.eng.exit()



if __name__ == '__main__':
    m = Math()
    m.resize('D:\\УМНИК\\Predobrab\\25718.png')

