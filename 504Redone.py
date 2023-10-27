from manim import*
import pandas as pd
import random as rnd

data =pd.read_excel('ExcelData.xlsx')
class diff(Scene):
    def construct(self):
        v=ValueTracker(0)
        t=ValueTracker(0)
        k=ValueTracker(0)
        title = Text("Bragg Diffraction").set_color_by_gradient(PURPLE_B,MAROON_C)
        self.play(Write(title))
        self.wait()
        self.play(ApplyWave(title),
                run_time=.9)
        title.generate_target()
        title.target.to_edge(UP).scale(.8)
        self.play(MoveToTarget(title))

        grid=NumberPlane(x_range=[-6,6],y_range=[-3,0]).shift(DOWN*2.5)
        grid2=always_redraw(lambda: NumberPlane(
            x_range=[-3.5,3.5],y_range=[-3,0])\
                .shift(DOWN*2.5).rotate(v.get_value()))
        grid3=always_redraw(lambda:NumberPlane(
            x_range=[-40,40],y_range=[-30,0],x_length=7,y_length=3)\
                .set_opacity(0.6).shift(DOWN*2.5).rotate(v.get_value()))
        samp=always_redraw(
            lambda:Rectangle(
                WHITE,height=1/10,width=1,fill_color=TEAL)\
                    .shift(DOWN*2).rotate(v.get_value()))
        samp_new=Rectangle(WHITE,height=1/10,width=1,fill_color=TEAL)\
            .shift(DOWN*2+LEFT*3.5).scale(.55)\
            .shift(UP)
        
        samp_dash=always_redraw(lambda:DashedLine(
            [-1,-2,0],[1.,-2,0],color=PURPLE_E)\
            .rotate(v.get_value()))
        samp_dash_new=DashedLine([-1,-2,0],[1.,-2,0],color=PURPLE_E)\
                    .shift(LEFT*3.5)\
                    .shift(UP)
        self.play(FadeIn(grid))
        dots=dict()
        var_index=0
        for x in range(-6, 6):
            for y in range(-3, 0):
                dots[f"{var_index}"] = Dot(np.array([x, y, 0]))
                var_index = var_index + 1
        self.play(FadeIn(*dots.values()))



        br=BraceBetweenPoints([2,-1,0],[2,-2,0],direction=RIGHT)
        param=MathTex("d").next_to(br,RIGHT,aligned_edge=LEFT).set_color(color=BLUE)

        eqn1=MathTex("n","\\lambda").next_to(grid,UP,DOWN).shift(UP*1.3 + LEFT)
        eqn2=MathTex("=","2","d","\\sin(","\\theta",")")\
            .next_to(eqn1,RIGHT,buff=1.26,aligned_edge=RIGHT)\
                .set_color_by_tex("d",color=BLUE).set_color_by_tex("\\theta",GREEN)
        brg_cond=Text("Bragg Condition").scale(.5).next_to(eqn1,UP,DOWN).shift(RIGHT*1.1+UP*1.3
        ).set_color_by_gradient(PURPLE_B,MAROON_B)
        
        self.play(Write(eqn1),run_time=.75)
        self.play(Write(eqn2),run_time=1)
        self.play(Write(brg_cond))
        self.play(FadeIn(br,param))


        inc=always_redraw(lambda:Line(
            [-4,0,0],[0,-2,0],color=RED_B)\
                .rotate(-1*t.get_value(),about_point=[0,-2,0]))
        inc_new=always_redraw(lambda:Line
            ([-6.5,-.5,0],[-3.5,-2,0],color=RED_B)\
                .shift(UP)
                .rotate(-1*k.get_value(),
                        about_point=[-3.5,-1,0]))\
                    

        sca=always_redraw(lambda:Line(
            [0,-2,0],[4,0,0],color=RED_B)\
                .rotate(t.get_value(),about_point=[0,-2,0]))
        sca_new=always_redraw(lambda:Line(
            [-3.5,-2,0],[-.5,-.5,0],color=RED_B)\
                .shift(UP)\
                .rotate(k.get_value(),
                        about_point=[-3.5,-1,0]))\
                

        sca2=always_redraw(
                lambda:Line(
                [0,-2,0],[4,0,0],
                color=RED_B)\
                .rotate(t.get_value(),
                about_point=[0,-2,0]))
        dashed= always_redraw(lambda:DashedLine(
            [0,-2,0],[4,-4,0],color=RED_B)\
                .rotate(-1*t.get_value(),about_point=[0,-2,0]))
        dashed_new= always_redraw(lambda:DashedLine(
            [-3.5,-1,0],[-.5,-2.5,0],color=RED_B)\
            .rotate(-1*k.get_value(),about_point=[-3.5,-1,0]))\
            

        text=Tex("Incident X-Ray").move_to([-4,1,0]).set_color_by_gradient(PURPLE_C,PURPLE_C,MAROON_D)
        text_new=Tex("Experiment").set_color_by_gradient(PURPLE_B,PURPLE_B,MAROON_C).move_to([-3.5,2,0])
        
        
        
        def opacity_setter(mob):
            randNum=rnd.random()
            mob.set_opacity(randNum)
        sca2.add_updater(opacity_setter)
        


        text2=Tex("Diffracted X-Ray").move_to([4,1,0]).set_color_by_gradient(MAROON_D,MAROON_D,PURPLE_C)
        text2_new=Tex("XRD Data").set_color_by_gradient(MAROON_C,MAROON_C,PURPLE_B).move_to([3.5,2,0])
        self.play(Create(inc),FadeIn(text))
        #self.play(FadeOut(text))
        self.play(Create(sca),FadeIn(text2))
        #self.play(FadeOut(text2))

        vg=(eqn1,eqn2)
        
        angle=MathTex("\\omega")\
            .set_color(YELLOW)\
                .shift(LEFT*1.3 + DOWN*1.74)
        angle_new=MathTex("\\omega")\
            .set_color(YELLOW)\
                .shift(LEFT*1.3 + DOWN*.74 +LEFT*3.5)

        angle2=MathTex("2","\\theta")\
            .set_color_by_tex("\\theta",GREEN)\
                .shift(RIGHT*1.4 + DOWN*1.95)
        angle2_new=MathTex("2","\\theta")\
            .set_color_by_tex("\\theta",GREEN)\
                .shift(RIGHT*1.4 + DOWN*.95 +LEFT*3.5)

        ang=always_redraw(
            lambda:Angle(Line([0,-2,0],[-4,0,0])\
                    .rotate(-1*t.get_value(),
                            about_point=[0,-2,0]),
                    Line([-1,-2,0],[1,-2,0])\
                    .rotate(v.get_value()),
                    radius=1,
                    quadrant=(1,-1)))
        ang_new=always_redraw(
            lambda:Angle(Line([-3.5,-1,0],[-7.5,1,0])\
                    
                    .rotate(-1*k.get_value(),
                            about_point=[-3.5,-1,0]),
                    Line([-4.5,-1,0],[-2.5,-1,0])\
                    .rotate(v.get_value()),
                    radius=1,
                    quadrant=(1,-1)))\
                    

        ang2=always_redraw(
            lambda:Angle(Line([0,-2,0],[4,-4,0])\
                    .rotate(-1*t.get_value(),
                            about_point=[0,-2,0]),
                    Line([0,-2,0],[4,0,0])\
                    .rotate(1*t.get_value(),
                            about_point=[0,-2,0]),
                    radius=1,quadrant=(1,11)))
        ang2_new=always_redraw(
            lambda:Angle(Line([-3.5,-1,0],[.5,-3,0])\
                    
                    .rotate(-1*k.get_value(),
                            about_point=[-3.5,-1,0]),
                    Line([-3.5,-1,0],[.5,1,0])\
                    .rotate(1*k.get_value(),
                            about_point=[-3.5,-1,0]),
                            radius=1,
                            quadrant=(1,11)))\
                    

        self.play(Create(ang))
        self.play(Write(angle))
        self.play(Create(dashed))
        self.play(Create(ang2),Write(angle2))
        self.wait()
        
        rect=Rectangle(height=7.5,width=12,fill_color=BLACK,fill_opacity=1
        ).set_color_by_gradient([TEAL,ORANGE,PINK]
        ).set_fill(DARKER_GREY)

        txt1=VGroup(
            MathTex("NOTE:"),
            MathTex(r"\text{If we hold 2}","\\theta","\\text{ constant while we vary }","\\omega","\\text{, we can}",color=WHITE),
            MathTex(r"\text{preform an }", "\\omega","\\text{ scan.}",color=WHITE),
            MathTex(r"\text{--}"),
            MathTex(r"\text{Since 2}","\\theta","\\text{ is constant, we are sampling the same}",color=WHITE),
            MathTex(r"\text{d-spacing throughout the scan, per Bragg's Law.}",color=WHITE),
            MathTex(r"\text{This is used to interrogate the quality of the crystal}",color=WHITE),
            MathTex(r"\text{--}"),
            MathTex(r"\text{*The angle shown is exaggerated for illustration}",color=WHITE).scale(0.7)
        ).arrange(DOWN,aligned_edge=LEFT)
        txt1.height=config.frame_height-2
        txt1.width=rect.width - 1

        self.wait(3)
        self.play(FadeIn(rect,txt1))
        self.wait(15)
        self.play(FadeOut(rect,txt1))

        wscan=MathTex("Omega\,  (\\omega) \,  Scan")\
                    .set_color_by_gradient(PURPLE_B,MAROON_C)\
                    .scale(1.6).to_edge(UP)


        self.play(FadeOut(
                        *dots.values(),br,param),
                FadeOut(eqn1,eqn2,brg_cond),
                ReplacementTransform(grid,samp))
        self.play(Transform(title,wscan),
                    Create(samp_dash))
        self.add(sca2)
        self.remove(sca)
        self.play(v.animate.set_value(-0.6/6),
                    run_time=1.5)
        self.play(v.animate.set_value(PI/(10)),
                    run_time=4.5,
                    rate_func=linear)
        self.add(sca)
        self.remove(sca2)
        self.wait(2)
        
        txt2= VGroup(
            MathTex("NOTE:"),
            MathTex(r"\text{If we set }","\\omega","\\text{ to always be equal to }","\\theta",color=WHITE),
            MathTex(r"\text{while varying 2}","\\theta","\\text{, we can do what",color=WHITE),
            MathTex(r"\text{is called a 2}", "\\theta","\\text{ scan}",color=WHITE),
            MathTex(r"\text{--}"),
            MathTex(r"\text{Using Bragg's Law, larger 2}","\\theta", "\\text{ values}",color=WHITE),
            MathTex(r"\text{correspond to planes with smaller}", "\\text{ d-spacings}",color=WHITE)
        ).arrange(DOWN,aligned_edge=LEFT)
        txt2.height=rect.height -1
        txt2.width=rect.width -1

        self.play(FadeIn(rect,txt2))
        self.wait(10)
        self.play(FadeOut(rect,txt2))

        self.play(v.animate.set_value(0),run_time=0.75)
        twothetascan=MathTex("2 Theta (2 \\theta) Scan")\
                    .set_color_by_gradient(PURPLE_B,MAROON_C)\
                    .scale(1.6)\
                    .to_edge(UP)

        self.play(ReplacementTransform(title,twothetascan))
        vgrpL=VGroup(sca,inc,samp,ang,ang2,angle,angle2,dashed,samp_dash,text,text2)
        vgrpL_new=VGroup(
                sca_new,inc_new,samp_new,ang_new,ang2_new,angle_new,
                angle2_new,dashed_new,samp_dash_new,text_new,text2_new)

        
        
        
        
        axes = Axes([10,119,10],[0,7],
                    axis_config={"include_numbers":True,
                                "exclude_origin_tick":True,
                                "font_size":28,
                                "include_tip":False},
                    y_axis_config={"scaling":LogBase(custom_labels=True)},
                    x_length=config.frame_width - 3,
                    y_length=config.frame_height-1.35)
        x=data["Two theta"]
        y=data["intensity"]
        xlabel=MathTex(r"2\theta \text{ (Theta)}").scale(.8).next_to(axes,DOWN)
        ylabel=Tex("Intensity (a.u.)").rotate(PI/2).scale(.8).next_to(axes,LEFT)
        line = axes.plot_line_graph(x,y,
                    add_vertex_dots=False,
                    stroke_width=.75,
                    line_color=LIGHT_PINK)
        SweepRect=always_redraw(
                    lambda:Rectangle(
                    height=axes.get_height()-.4,
                    width=.2,
                    color=GREY,
                    fill_opacity=.33,
                    stroke_width=.3)\
                    .next_to(axes,LEFT,buff=-1).shift(((360*t.get_value()/PI))*RIGHT/10.5))
        vgrpR=VGroup(axes,xlabel,ylabel,line,SweepRect).scale(.58).shift(RIGHT*3.5)
        
        self.play(ReplacementTransform(vgrpL,vgrpL_new),
                    FadeIn(vgrpR))
        self.play(k.animate.set_value(-.4636476+PI/9))

        self.wait(2)
        
        sca_new.add_updater(opacity_setter)
        self.play(k.animate.set_value(-.4636476+PI/4 + PI/9),t.animate.set_value(PI/6.1),run_time=10,rate_func=linear)
        self.wait(3)
        
        
