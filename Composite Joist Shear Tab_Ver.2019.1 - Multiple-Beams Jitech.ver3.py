# startup code begin
import os
from param import *
from math import *
Units("feet")
saved_sds2_version = '2017.21'
saved_python_version = (2, 7, 2, 'final', 0)
try:
    from shape import Shape
    from point import Point, PointLocate
    from member import Member, MemberLocate
    from mtrl_list import MtrlLocate, HoleLocate
    from cons_line import ConsLine
    from cons_circle import ConsCircle
    from rnd_plate import RndPlate
    from rect_plate import RectPlate
    from bnt_plate import BntPlate
    from rolled_section import RolledSection
    from weld_add import Weld
    from flat_bar import FlatBar
    from hole_add import Hole
    from bolt_add import Bolt
    from roll_plate import RollPl
    from sqr_bar import SqrBar
    from rnd_bar import RndBar
    from shr_stud import ShrStud
    from grate import Grate
    from grate_trd import GrateTrd
    from deck import Deck
    from mtrl_fit import MtrlFit
    from version import CurrentVersion, VersionCompare
    curr_version = CurrentVersion()
except ImportError:
    curr_version = 'None' 
    def VersionCompare( v1, v2 ):
        return -1
if VersionCompare( curr_version, '6.311' ) >= 0:
    from job import Job
    from fab import Fabricator
if VersionCompare( curr_version, '6.312' ) >= 0:
    from plate_layout import PlateLayout
if VersionCompare( curr_version, '6.314' ) >= 0:
    from plate_layout import BntPlateLayout
if VersionCompare( curr_version, '6.4' ) >= 0:
    from mtrl_cut import MtrlCut
if VersionCompare( curr_version, '7.006' ) >= 0:
    from member import MemberAllocated
if VersionCompare( curr_version, '7.009' ) >= 0:
    from job import JobName
    from fab import FabricatorName
if VersionCompare( curr_version, '7.1' ) >= 0:
    from job import ProcessJob
    from job import ProcessOneMem
    from view import View
    from clevis import Clevis
    from turnbuckle import Turnbuckle
    from member import MultiMemberLocate
    from mtrl_list import MtrlByGuid
if VersionCompare( curr_version, '7.101' ) >= 0:
    from member import MemberProperties
    from member import MemberPropertySet
if VersionCompare( curr_version, '7.109' ) >= 0:
    from assembly import Assembly
    from assembly import AssemblyList
if VersionCompare( curr_version, '7.110' ) >= 0:
    from member import GroupMemberCreate
if VersionCompare( curr_version, '7.113' ) >= 0:
    from member import MarkMemberForProcess
if VersionCompare( curr_version, '7.132' ) >= 0:
    from mtrl_list import MtrlProperties
    from mtrl_list import MtrlPropertySet
    from job import JobProperties
    from job import JobPropertySet
# startup code end

#BEAM = Framing Member
#P0 = Joist-Beam Framing Point
#P1 = Beam End Location
#JOIST = Joist that frames
#JWEB = Joist Web
#PL_THCK = Shear Tab Thickness
#PL_EXT2 = Plate Extent to
#PL_EPF = Extend Past Flange
#PL_HED = Plate Horizontal Edge Distance
#S_FCT = Shear Tab Side Factor
#PL_GRD = Shear Tab Plate Grade
#FSTDX = First Bolt Horizontal Dimension
#FSTDY = First Boldt Vertical Dimension
#DIAM = Bolt Diameter
#HOLE_TYP = Hole Type
#BL_GRD = Bolt Grade
#COLS = Number of columns of holes
#SPCX = Spacing X Holes
#SPCY = Spacing Y Holes
#FACT = Rotation Factor

#Default Variables
#pl_thck = 0.5
#bolt_dia = 0.75
typ_cnx = 'Plate'
typ_cnx2 = 'Plate'
pl_grade = 'A36'
pl_grade2 = 'A36'
ang_mtrl = 'L5x3x3/8'
ang_mtrl2 = 'L5x3x3/8'
pl_side = "NS"
pl_side2 = "NS"
top_cp = "No"
top_cp2 = "No"
btm_cp = "No"
btm_cp2 = "No"
ext_to = 'Both Flanges'
ext_to2 = 'Both Flanges'
bolt_grade = 'A325N'
bolt_grade2 = 'A325N'
hole_type = 'Standard Round'
hole_type2 = 'Standard Round'
st_s1 = 1
st_s2 = 1
image_file_path = os.path.join(os.getcwd(), "macro", "Images", "Composite_Joist.PNG")
image_file_path2 = os.path.join(os.getcwd(), "macro", "Images", "Composite_Joist_Angle.PNG")

#List Definition
#pl_thckList = ['1/2','5/8','3/4','7/8','1']
#bolt_diaList = ['1/2','5/8','3/4','7/8','1']
pl_gradeList = ['A36','A572-50','A572-60']
bolt_gradeList = ['A325N','A490N','F1852N','F2280N']
ext_toList = ['Both Flanges', 'Both Ks', 'Top Flange & Bottom K', 'Top K & Bottom Flange', 'Depth', 'Height']
hole_typeList = ['Standard Round', 'Short slot', 'Oversized round', 'Long slot']

#Functions Definition
#Function starts
def CJ_SHEARTAB (BEAM, P0, P1, JOIST, JWEB, PLJ_WIDTH, PL_THCK, PL_EXT2, DP_HG, KCK_OFF, PL_EPF, PL_TC, PL_TCL, PL_TCD, PL_BC, PL_BCL, PL_BCD, FL_CLR, PL_HED, PL_VED, PL_GRD, S_FACT, FSTDX, FSTDY, AFSTDX, AFSTDY, AFSTDXS, AFSTDYS, DIAM, DIAM_S, BH_TYP, BL_GRD, COLS, ROWS, COLS_S, ROWS_S, SPCX, SPCY, SPCX_S, SPCY_S, WLD_SZE, PL_ANGL, ANGLE_MAT, FACT):
    if PL_ANGL == 'Plate':
        #print(P0.x)
        p1 = RectPlate()
        p1.Member = BEAM
        if BEAM.Type == "Beam":
            if mem1.PlaneAngleOfRotation == 90:
                p1.Point1 = P1 + BEAM.TranslateToGlobal((P0.x - P1.x) - S_FACT*((JWEB + PL_THCK)*0.5), 0, -FACT*BEAM.tw*0.5)
            else:
                p1.Point1 = P1 + BEAM.TranslateToGlobal((P0.y - P1.y) + S_FACT*((JWEB + PL_THCK)*0.5), 0, FACT*BEAM.tw*0.5)
            #print("Beam")
        elif BEAM.Type == "Column":
            if mem1.PlaneAngleOfRotation == 90:
                p1.Point1 = P1 + BEAM.TranslateToGlobal((P0.z + 5) - P1.z, S_FACT*((JWEB + PL_THCK)*0.5), -FACT*BEAM.tw*0.5)# 5 is the bearing depth
            else:
                p1.Point1 = P1 + BEAM.TranslateToGlobal((P0.z + 5) - P1.z, -S_FACT*((JWEB + PL_THCK)*0.5), FACT*BEAM.tw*0.5)# 5 is the bearing depth
        p1.Point2 = p1.Point1 + (BEAM.depth, 0,0)
        p1.MaterialGrade = PL_GRD
        p1.MaterialOriginPoint = "Center"
        if PL_EXT2 == 'Both Flanges':
            p1.TopOperationTypeLeftEnd = "Clip"
            p1.TopOperationTypeRightEnd = "Clip"
        elif PL_EXT2 == 'Both Ks':
            p1.TopOperationTypeLeftEnd = "None"
            p1.TopOperationTypeRightEnd = "None"
        elif PL_EXT2 == 'Top Flange & Bottom K':
            p1.TopOperationTypeLeftEnd = "Clip"
            p1.TopOperationTypeRightEnd = "None"
        elif PL_EXT2 == 'Top K & Bottom Flange':
            p1.TopOperationTypeLeftEnd = "None"
            p1.TopOperationTypeRightEnd = "Clip"
        elif PL_EXT2 == 'Height':
            p1.TopOperationTypeLeftEnd = "None"
            p1.TopOperationTypeRightEnd = "Clip"
        elif PL_EXT2 == 'Depth':
            p1.TopOperationTypeLeftEnd = "Clip"
            p1.TopOperationTypeRightEnd = "None"                
        p1.TopLengthLeft = BEAM.k - BEAM.tf
        p1.TopLengthRight =  BEAM.k - BEAM.tf
        p1.TopClipLeft = p1.TopLengthLeft
        p1.TopClipRight = p1.TopLengthRight
        if PL_EPF.count('Extend past flange') == 1:
            p1.width = BEAM.bf*0.5 - BEAM.tw*0.5 + FL_CLR + (COLS - 1) * SPCY + 2 * PL_HED #ADDED
            if PL_TC == 'No':
                p1.BottomOperationTypeLeftEnd = "None"
            else:
                p1.BottomOperationTypeLeftEnd = "Cope"
                if (FSTDY - BEAM.tf - PL_VED) <= 0:
                    p1.BottomLengthLeft = 0
                else:
                    p1.BottomLengthLeft = FSTDY - BEAM.tf - PL_VED
                #p1.BottomLengthLeft = PL_TCL
                p1.BottomCopeLeft = p1.Width - BEAM.bf*0.5 + BEAM.tw*0.5 + 0.5 #PL_TCD

            if PL_BC == 'No':
                p1.BottomOperationTypeRightEnd = "None"
            else:
                p1.BottomOperationTypeRightEnd = "Cope"
                if (BEAM.depth - FSTDY  - (ROWS - 1)*SPCX - PL_VED - BEAM.tf) <= 0:
                    p1.BottomLengthRight = 0
                else:
                    p1.BottomLengthRight = BEAM.depth - FSTDY  - (ROWS - 1)*SPCX - PL_VED - BEAM.tf #PL_BCL
                #p1.BottomLengthRight = PL_BCL
                p1.BottomCopeRight = p1.Width - BEAM.bf*0.5 + BEAM.tw*0.5 + 0.5 #PL_BCD            
        else:
            p1.Width = FL_CLR + FSTDX + (COLS -1)*SPCY + PL_HED  #ADDED modified on 01-11-2020
            if p1.Width <= (BEAM.bf*0.5 - BEAM.tw*0.5):
                p1.BottomOperationTypeLeftEnd = "None"
                p1.BottomOperationTypeRightEnd = "None"
            else:
                if PL_TC == 'No':
                    p1.BottomOperationTypeLeftEnd = "None"
                else:
                    p1.BottomOperationTypeLeftEnd = "Cope"
                    if (FSTDY - BEAM.tf - PL_VED) <= 0:
                        p1.BottomLengthLeft = 0
                    else:
                        p1.BottomLengthLeft = FSTDY - BEAM.tf - PL_VED
                    p1.BottomCopeLeft = p1.Width - BEAM.bf*0.5 + BEAM.tw*0.5 + 0.5
                    
                if PL_BC == 'No':
                    p1.BottomOperationTypeRightEnd = "None"
                else:
                    p1.BottomOperationTypeRightEnd = "Cope"
                    if (BEAM.depth - FSTDY  - (ROWS - 1)*SPCY - PL_VED - BEAM.tf) <= 0: #modified on 01-11-2020
                        p1.BottomLengthRight = 0
                    else:
                        p1.BottomLengthRight = BEAM.depth - FSTDY  - (ROWS - 1)*SPCY - PL_VED - BEAM.tf #PL_BCL
                    p1.BottomCopeRight = p1.Width - BEAM.bf*0.5 + BEAM.tw*0.5 + 0.5
        p1.Thickness = PL_THCK
        p1.WorkpointSlopeDistance = p1.Point1.Distance(p1.Point2)
        if BEAM.Type == "Beam":
            if PL_EXT2 == 'Both Flanges':
                p1.MaterialSetbackLeftEnd = BEAM.tf
                p1.MaterialSetbackRightEnd = BEAM.tf
            elif PL_EXT2 == 'Both Ks':
                p1.MaterialSetbackLeftEnd = BEAM.k
                p1.MaterialSetbackRightEnd = BEAM.k
            elif PL_EXT2 == 'Top Flange & Bottom K':
                p1.MaterialSetbackLeftEnd = BEAM.tf
                p1.MaterialSetbackRightEnd = BEAM.k
            elif PL_EXT2 == 'Top K & Bottom Flange':
                p1.MaterialSetbackLeftEnd = BEAM.k
                p1.MaterialSetbackRightEnd = BEAM.tf
            elif PL_EXT2 == 'Height':
                #print('Height')
                p1.MaterialSetbackLeftEnd = BEAM.depth - DP_HG
                p1.MaterialSetbackRightEnd = BEAM.tf
            elif PL_EXT2 == 'Depth':
                #print('Depth')
                p1.MaterialSetbackLeftEnd = BEAM.tf
                p1.MaterialSetbackRightEnd = BEAM.depth - DP_HG
        else:
            p1.MaterialSetbackLeftEnd = 0
            p1.MaterialSetbackRightEnd = BEAM.depth - DP_HG
        p1.WebCutLeftEnd = 0
        p1.WebCutRightEnd = 0
        p1.OrderLength = p1.WorkpointSlopeDistance - p1.MaterialSetbackLeftEnd - p1.MaterialSetbackRightEnd
        p1.MaterialType = "Plate"
        p1.SurfaceFinish = "Red oxide"
        p1.MaterialColor3d = "Medium_material"
        p1.ReferencePointOffset = (0, 0, 0)
        p1.Add()
        if BEAM.Type == "Beam":
            if mem1.PlaneAngleOfRotation == 90:
                p1.Rotate(p1.Member, (FACT*90, 0, -90))
            else:
                p1.Rotate(p1.Member, (-FACT*90, 0, -90))
            #print("Beam")
        elif BEAM.Type == "Column":
            if mem1.PlaneAngleOfRotation == 90:
                p1.Rotate(p1.Member, (FACT*90, 0, 180))
            else:
                p1.Rotate(p1.Member, (-FACT*90, 0, 180))
            #print("Column")
        else:
            print("No supported member type")
        #joist plate begins
        p2 = RectPlate()
        p2.Member = JOIST
        if BEAM.Type == "Beam":
            #print("Beam")
            if PL_EPF.count('Extend past flange') == 1:
                if mem1.PlaneAngleOfRotation == 90:
                    p2.Point1 = P1 + BEAM.TranslateToGlobal((P0.x - P1.x), 0, -FACT*(BEAM.bf*0.5 + FL_CLR))
                    #p2.Point2 = p2.Point1 + (JOIST.depth, 0,0)
                else:
                    p2.Point1 = P1 + BEAM.TranslateToGlobal((P0.y - P1.y), 0, FACT*(BEAM.bf*0.5 + FL_CLR))
                    #p2.Point2 = p2.Point1 + (JOIST.depth, 0,0)
                #p2.Point2 = p2.Point1 + (JOIST.depth, 0,0)
            else:
                if mem1.PlaneAngleOfRotation == 90:
                    p2.Point1 = P1 + BEAM.TranslateToGlobal((P0.x - P1.x), 0, -FACT*(BEAM.tw*0.5 + FL_CLR))
                    #p2.Point2 = p2.Point1 + (FSTDY + (ROWS-1)*SPCY + PL_VED, 0,0)
                else:
                    p2.Point1 = P1 + BEAM.TranslateToGlobal((P0.y - P1.y), 0, FACT*(BEAM.tw*0.5 + FL_CLR))
                    #p2.Point2 = p2.Point1 + (FSTDY + (ROWS-1)*SPCY + PL_VED, 0,0)
                #p2.Point2 = p2.Point1 + (FSTDY + (ROWS-1)*SPCY + PL_VED, 0,0)
        elif BEAM.Type == "Column":
            #print("Column")
            if PL_EPF.count('Extend past flange') == 1:
                if mem1.PlaneAngleOfRotation == 90:
                    p2.Point1 = P1 + BEAM.TranslateToGlobal((P0.z + 5) - P1.z, 0, -FACT*(BEAM.bf*0.5 + FL_CLR))
                    #p2.Point2 = p2.Point1 + (JOIST.depth, 0,0)
                else:
                    p2.Point1 = P1 + BEAM.TranslateToGlobal((P0.z + 5) - P1.z, 0, FACT*(BEAM.bf*0.5 + FL_CLR))
                    #p2.Point2 = p2.Point1 + (JOIST.depth, 0,0)
                #p2.Point2 = p2.Point1 + (JOIST.depth, 0,0)
            else:
                if mem1.PlaneAngleOfRotation == 90:
                    p2.Point1 = P1 + BEAM.TranslateToGlobal((P0.z + 5) - P1.z, 0, -FACT*(BEAM.tw*0.5 + FL_CLR))
                    #p2.Point2 = p2.Point1 + (FSTDY + (ROWS-1)*SPCY + PL_VED, 0,0)
                else:
                    p2.Point1 = P1 + BEAM.TranslateToGlobal((P0.z + 5) - P1.z, 0, FACT*(BEAM.tw*0.5 + FL_CLR))
                    #p2.Point2 = p2.Point1 + (FSTDY + (ROWS-1)*SPCY + PL_VED, 0,0)
                #p2.Point2 = p2.Point1 + (FSTDY + (ROWS-1)*SPCY + PL_VED, 0,0)
        p2.Point2 = p2.Point1 + (JOIST.depth, 0,0)
        p2.MaterialGrade = PL_GRD
        p2.MaterialOriginPoint = "Center"
        p2.TopOperationTypeLeftEnd = "None"
        p2.TopOperationTypeRightEnd = "None"
        p2.BottomOperationTypeLeftEnd = "None"
        p2.BottomOperationTypeLeftEnd = "None"
        if PLJ_WIDTH >= FSTDX + (COLS - 1)*SPCX + 6: #TO ADD 6 INCHES OR NOT
            p2.Width = PLJ_WIDTH
        else:
            p2.Width = FSTDX + (COLS - 1)*SPCX + 6 #TO ADD 6 INCHES OR NOT
        p2.Thickness = JWEB
        p2.WorkpointSlopeDistance = p2.Point1.Distance(p2.Point2)
        if PL_EPF.count('Extend past flange') == 1:
            p2.MaterialSetbackLeftEnd = 0
            p2.MaterialSetbackRightEnd = 0
        else:
            if KCK_OFF.count('Kicker Off') == 1:
                p2.MaterialSetbackLeftEnd = BEAM.tf + 0.4375 #flange thickness + 7/16gap (5/16 +1/8)
                p2.MaterialSetbackRightEnd = JOIST.depth - FSTDY - (ROWS-1)*SPCX - PL_VED     #modified on 01-11-2020           
            else:
                p2.MaterialSetbackLeftEnd = BEAM.tf + 0.4375 #flange thickness + 7/16gap (5/16 +1/8)
                p2.MaterialSetbackRightEnd = BEAM.tf + 0.4375 #flange thickness + 7/16gap (5/16 +1/8)
                p2.TopOperationTypeRightEnd = "None"
                p2.TopLengthRight =  JOIST.depth - (p2.MaterialSetbackRightEnd + FSTDY + (ROWS-1)*SPCX + PL_VED)
                p2.TopCopeRight = BEAM.bf*0.5 - BEAM.tw*0.5
        p2.WebCutLeftEnd = 0
        p2.WebCutRightEnd = 0
        p2.OrderLength = p2.WorkpointSlopeDistance - p2.MaterialSetbackLeftEnd - p2.MaterialSetbackRightEnd
        p2.MaterialType = "Plate"
        p2.SurfaceFinish = "Red oxide"
        p2.MaterialColor3d = "Medium_material"
        p2.ReferencePointOffset = (0, 0, 0)
        p2.Add()
        p2.Rotate(p2.Member, (90 + FACT*90, 0, -90))
        #joist plate ends
        #hole group add begins
        hole1 = Hole()
        hole1.Material = [p1, ]
        if PL_EPF.count('Extend past flange') == 1:
            hole1.Point = hole1.Material.Location + hole1.Material.TranslateToGlobal( FSTDY, -((BEAM.bf - BEAM.tw)*0.5 + FL_CLR + PL_HED), 0 )
        else:
            hole1.Point = hole1.Material.Location + hole1.Material.TranslateToGlobal( FSTDY, -(FSTDX + FL_CLR), 0 )
        hole1.Type = 'Standard Round'
        hole1.Matchable = 'Yes'
        hole1.MaterialFace = 'FS Face'
        hole1.ShouldBeValid = 'Yes'
        hole1.ReferenceOffsetX = 0
        hole1.ReferenceOffsetY = 0
        hole1.SpacingX = SPCX
        hole1.SpacingY = SPCY
        hole1.GroupRotation = 0
        hole1.Locate = 'Above Right'
        hole1.Columns = ROWS
        hole1.Rows = COLS
        hole1.BoltType = BL_GRD
        hole1.PlugType = 'No Plug'
        hole1.BoltDiameter = DIAM
        hole1.SlotRotation = 90
        hole1.SlotLength = hole1.calc_slot_length()
        hole1.Diameter = hole1.CalculateHoleSize()
        hole1.BothSides = 'Yes'
        hole1.ShowWindow = 'Yes'
        hole1.Create()
        #hole group add ends
        #match hole group add begins
        hole2 = Hole()
        hole2.Material = [p2, ]
        hole2.Holes = [hole1, ]
        hole2.Type = BH_TYP
        hole2.Matchable = 'Yes'
        hole2.ShouldBeValid = 'Yes'
        hole2.Diameter = hole1.calc_hole_size()
        hole2.BothSides = 'Yes'
        hole2.ShowWindow = 'Yes'
        hole2.Create()
        #match hole group add ends
        #bolt add begins
        bolt1 = Bolt()
        bolt1.Material = [p2, ]
        bolt1.Match = [p1, ]
        bolt1.Diameter = DIAM
        bolt1.PrimaryNutType = "Heavy hex"
        bolt1.SecondaryNutType = "None"
        bolt1.BoltType = BL_GRD
        bolt1.IsFieldBolt = "Field"
        bolt1.IsTensionControl = "No"
        bolt1.Finish = "Black"
        bolt1.PrimaryHeadWasher.TypeDescription = "None"
        bolt1.PrimaryHeadWasher.GradeDescription = "F436"
        bolt1.PrimaryHeadWasher.Quantity = 0
        bolt1.PrimaryHeadWasher.Thickness = 0
        bolt1.PrimaryHeadWasher.Width = 0
        bolt1.PrimaryHeadWasher.Rotation = 0
        bolt1.SecondaryHeadWasher.TypeDescription = "None"
        bolt1.SecondaryHeadWasher.GradeDescription = "F436"
        bolt1.SecondaryHeadWasher.Quantity = 0
        bolt1.SecondaryHeadWasher.Thickness = 0
        bolt1.SecondaryHeadWasher.Width = 0
        bolt1.SecondaryHeadWasher.Rotation = 0
        bolt1.TertiaryHeadWasher.TypeDescription = "None"
        bolt1.TertiaryHeadWasher.GradeDescription = "F436"
        bolt1.TertiaryHeadWasher.Quantity = 0
        bolt1.TertiaryHeadWasher.Thickness = 0
        bolt1.TertiaryHeadWasher.Width = 0
        bolt1.TertiaryHeadWasher.Rotation = 0
        bolt1.PrimaryNutWasher.TypeDescription = "Hardened"
        bolt1.PrimaryNutWasher.GradeDescription = "F436"
        bolt1.PrimaryNutWasher.Quantity = 1
        bolt1.PrimaryNutWasher.Thickness = 4
        bolt1.PrimaryNutWasher.Width = 38
        bolt1.PrimaryNutWasher.Rotation = 0
        bolt1.SecondaryNutWasher.TypeDescription = "None"
        bolt1.SecondaryNutWasher.GradeDescription = "F436"
        bolt1.SecondaryNutWasher.Quantity = 0
        bolt1.SecondaryNutWasher.Thickness = 0
        bolt1.SecondaryNutWasher.Width = 0
        bolt1.SecondaryNutWasher.Rotation = 0
        bolt1.TertiaryNutWasher.TypeDescription = "None"
        bolt1.TertiaryNutWasher.GradeDescription = "F436"
        bolt1.TertiaryNutWasher.Quantity = 0
        bolt1.TertiaryNutWasher.Thickness = 0
        bolt1.TertiaryNutWasher.Width = 0
        bolt1.TertiaryNutWasher.Rotation = 0
        bolt1.ShowWindow = "No"
        bolt1.Direction = "Out"
        bolt1.AddMatch()
        #bolt add ends
        #weld add begin
        weld1 = Weld()
        weld1.Material = [p1, ]
        weld1.WeldTo = [BEAM, ]
        weld1.ArrowSize = WLD_SZE
        weld1.OtherSize = WLD_SZE
        weld1.FieldWeld = 'No'
        weld1.WeldAllAround = 'No'
        weld1.SpacerBarRequired = 'No'
        weld1.NonPrequalifiedWeld = 'Yes'
        weld1.JointType = 'None'
        weld1.Penetration = 'None'
        weld1.Process = 'None'
        weld1.Position = 'None'
        weld1.MaximumGap = 0
        weld1.WeldInside = 'No'
        weld1.one_weld_per_segment = 'No'
        if p1.Width < (BEAM.bf*0.5 - BEAM.tw*0.5):
            weld1.min_length = p1.Width - BEAM.k
        else:
            weld1.min_length = BEAM.bf*0.5 - BEAM.k
        weld1.generate_fillet = 'No'
        weld1.generate_flare = 'No'
        weld1.generate_plug = 'No'
        weld1.generate_v_groove = 'No'
        weld1.generate_bevel_groove = 'No'
        weld1.ArrowWeldType = 'Fillet'
        weld1.ArrowLeftSetback = 0
        weld1.ArrowRightSetback = 0
        weld1.ArrowRootFace = 0
        weld1.ArrowRootOpening = 0
        weld1.arrow_effective_throat = 0
        weld1.ArrowWeldContourDescription = 'None'
        weld1.ArrowGrooveAngle = 0
        weld1.ArrowFilletBackupWeld = 'No'
        weld1.Stitch = 'No'
        weld1.ArrowStitchLength = 0
        weld1.ArrowStitchSpacing = 0
        weld1.ArrowLeftTermination = 0
        weld1.ArrowRightTermination = 0
        weld1.OtherWeldTypeIndex = 'Fillet'
        weld1.OtherLeftSetback = 0
        weld1.OtherRightSetback = 0
        weld1.OtherRootFace = 0
        weld1.OtherRootOpening = 0
        weld1.other_effective_throat = 0
        weld1.OtherContour = 'None'
        weld1.OtherGrooveAngle = 0
        weld1.OtherFilletBack = 'No'
        weld1.other_stitch = 'None'
        weld1.OtherStitchLength = 0
        weld1.OtherStitchSpacing = 0
        weld1.OtherLeftTermination = 0
        weld1.OtherRightTermination = 0
        weld1.WeldSymbolTailText = "TYP"
        weld1.ShowWindow = 'No'
        weld1.Create()
        #weld add end        
    else:
        #print('Angle')
        rl2 = RolledSection()
        rl2.Member = BEAM
        if FACT == 1:
            if mem1.PlaneAngleOfRotation == 90:
                if S_FACT == -1:
                    rl2.Point1 = rl2.Member.LeftEnd.Location + rl2.Member.TranslateToGlobal( (P0.x - P1.x) + 0.5, 0, -BEAM.tw*0.5 )
                else:
                    rl2.Point1 = rl2.Member.LeftEnd.Location + rl2.Member.TranslateToGlobal( (P0.x - P1.x) - 0.5, 0, -BEAM.tw*0.5 )
            else:
                if S_FACT == -1:
                    rl2.Point1 = rl2.Member.LeftEnd.Location + rl2.Member.TranslateToGlobal( (P0.y - P1.y) - 0.5, 0, BEAM.tw*0.5 )
                else:
                    rl2.Point1 = rl2.Member.LeftEnd.Location + rl2.Member.TranslateToGlobal( (P0.y - P1.y) + 0.5, 0, BEAM.tw*0.5 )                    
        else:
            if mem1.PlaneAngleOfRotation == 90:
                if S_FACT == -1:
                    rl2.Point1 = rl2.Member.LeftEnd.Location + rl2.Member.TranslateToGlobal( (P0.x - P1.x) + 0.5, 0, BEAM.tw*0.5 )
                else:
                    rl2.Point1 = rl2.Member.LeftEnd.Location + rl2.Member.TranslateToGlobal( (P0.x - P1.x) - 0.5, 0, BEAM.tw*0.5 )
            else:
                if S_FACT == -1:
                    rl2.Point1 = rl2.Member.LeftEnd.Location + rl2.Member.TranslateToGlobal( (P0.y - P1.y) - 0.5, 0, -BEAM.tw*0.5 )
                else:
                    rl2.Point1 = rl2.Member.LeftEnd.Location + rl2.Member.TranslateToGlobal( (P0.y - P1.y)+ 0.5, 0, -BEAM.tw*0.5 )
        rl2.Point2 = rl2.Point1 + rl2.Member.TranslateToGlobal( 0, -BEAM.depth, 0 )
        rl2.SectionSize = ANGLE_MAT
        rl2.MaterialGrade = 'A36'
        rl2.Centered = 'No'
        rl2.TopOperationTypeLeftEnd = 'None'
        rl2.TopOperationTypeRightEnd = 'None'
        rl2.BottomOperationTypeLeftEnd = 'None'
        rl2.BottomOperationTypeRightEnd = 'None'
        rl2.IsLongLegVerticalMaterial = 'HZ.'
        if FACT == 1:
            if S_FACT == -1:
                rl2.ToeInOrOut = 'In'
            else:
                rl2.ToeInOrOut = 'Out'
        else:
            if S_FACT == -1:
                rl2.ToeInOrOut = 'Out'
            else:
                rl2.ToeInOrOut = 'In'
        rl2.RollType = 'None'
        rl2.FieldWeldPrepFlagLeftEnd = 'No'
        rl2.FieldWeldPrepFlagRightEnd = 'No'
        rl2.MomentConnectionWebSetbackLeftEnd = 0
        rl2.MomentConnectionWebSetbackRightEnd = 0
        rl2.MaterialTwistAngle = 0
        rl2.MidOrdinate = 0
        rl2.IncludedAngle = 0
        rl2.RollingRadius = 0
        rl2.SpiralOffset = 0
        rl2.WorkpointSlopeDistance = rl2.Point1.Distance(rl2.Point2)
        if AFSTDY >= AFSTDYS:
            rl2.MaterialSetbackLeftEnd = AFSTDYS - PL_VED
        else:
            rl2.MaterialSetbackLeftEnd = AFSTDY - PL_VED
            
        if AFSTDY + (ROWS - 1)*SPCX >= AFSTDYS + (ROWS_S - 1)*SPCX_S:            
            rl2.MaterialSetbackRightEnd = BEAM.depth - AFSTDY - (ROWS - 1)*SPCX - PL_VED
        else:            
            rl2.MaterialSetbackRightEnd = BEAM.depth - (AFSTDYS + (ROWS_S - 1)*SPCX_S + PL_VED)
        rl2.WebCutLeftEnd = 0
        rl2.WebCutRightEnd = 0
        rl2.FlangeCutLeftEnd = 0
        rl2.FlangeCutRightEnd = 0
        rl2.LeftEndPreparation = 'Standard cut'
        rl2.RightEndPreparation = 'Standard cut'
        rl2.OrderLength = rl2.WorkpointSlopeDistance - rl2.MaterialSetbackLeftEnd - rl2.MaterialSetbackRightEnd
        rl2.MaterialType = 'Angle'
        rl2.SurfaceFinish = 'Red oxide'
        rl2.MaterialColor3d = 'Plate'
        rl2.ReferencePointOffset = (0, 0, 0)
        rl2.Add()
        if mem1.PlaneAngleOfRotation == 90:
            if S_FACT == -1:
                rl2.Rotate(rl2.Member, (FACT*180, 0.000000, -90.000000)) #(90 + FACT*90, 0, -90))
            else:
                rl2.Rotate(rl2.Member, (0, 0.000000, -90.000000)) #(90 + FACT*90, 0, -90))
        else:
            if S_FACT == -1:
                rl2.Rotate(rl2.Member, (0, 0.000000, -90.000000)) #(90 + FACT*90, 0, -90))
            else:
                rl2.Rotate(rl2.Member, (FACT*180, 0.000000, -90.000000)) #(90 + FACT*90, 0, -90))
        #hole group add begin for SUPPORTED MEMBER
        hole3 = Hole()
        hole3.Material = [rl2, ]
        if FACT == 1:
            if S_FACT == -1:
                hole3.Point = hole3.Material.Location + hole3.Material.TranslateToGlobal( AFSTDY, -0.25, (AFSTDX - BEAM.tw*0.5) )
            else:
                hole3.Point = hole3.Material.Location + hole3.Material.TranslateToGlobal( AFSTDY, -0.25, -(AFSTDX - BEAM.tw*0.5) )
        else:
            if S_FACT == -1:
                hole3.Point = hole3.Material.Location + hole3.Material.TranslateToGlobal( AFSTDY, -0.25, -(AFSTDX - BEAM.tw*0.5) )
            else:
                hole3.Point = hole3.Material.Location + hole3.Material.TranslateToGlobal( AFSTDY, -0.25, (AFSTDX - BEAM.tw*0.5) )            
        hole3.Type = 'Standard Round'
        hole3.Matchable = 'Yes'
        hole3.MaterialFace = 'Web FS'
        hole3.ShouldBeValid = 'Yes'
        hole3.ReferenceOffsetX = 0
        hole3.ReferenceOffsetY = 0
        hole3.SpacingX = SPCX
        hole3.SpacingY = SPCY
        hole3.GroupRotation = 0
        hole3.Locate = 'Above Right'
        hole3.Columns = ROWS
        hole3.Rows = COLS
        hole3.BoltType = 'AUTO'
        hole3.PlugType = 'No Plug'
        hole3.BoltDiameter = DIAM
        hole3.Diameter = hole3.CalculateHoleSize()
        hole3.BothSides = 'Yes'
        hole3.ShowWindow = 'Yes'
        hole3.Create()
        # hole group add end for SUPPORTED MEMBER
        # hole group add begin for SUPPORTING MEMBER
        hole4 = Hole()
        hole4.Material = [rl2, ]
        hole4.Point = hole4.Material.Location + hole4.Material.TranslateToGlobal( AFSTDYS, -(AFSTDXS - 0.5), 0.25 ) #( bolt_fstdys, -(bolt_fstdxs - 0.5), 0.25 )
        hole4.Type = 'Standard Round'
        hole4.Matchable = 'Yes'
        hole4.MaterialFace = 'Bottom Face'
        hole4.ShouldBeValid = 'Yes'
        hole4.ReferenceOffsetX = 0
        hole4.ReferenceOffsetY = 0
        hole4.SpacingX = SPCX_S
        hole4.SpacingY = SPCY_S
        hole4.GroupRotation = 0
        hole4.Locate = 'Above Right'
        hole4.Columns = ROWS_S
        hole4.Rows = COLS_S
        hole4.BoltType = 'AUTO'
        hole4.PlugType = 'No Plug'
        hole4.BoltDiameter = DIAM_S
        hole4.Diameter = hole4.CalculateHoleSize()
        hole4.BothSides = 'Yes'
        hole4.ShowWindow = 'Yes'
        hole4.Create()
        # hole group add end for SUPPORTING MEMBER
        try:
            #match hole group add begins
            hole5 = Hole()
            hole5.Material = [BEAM.Material(0), ]
            hole5.Holes = [hole4, ]
            hole5.Type = 'Standard Round'
            hole5.Matchable = 'Yes'
            hole5.ShouldBeValid = 'Yes'
            hole5.Diameter = hole4.calc_hole_size()
            hole5.BothSides = 'Yes'
            hole5.ShowWindow = 'Yes'
            hole5.Create()
            #match hole group add ends
        except:
            pass
        #joist plate begins
        p2 = RectPlate()
        p2.Member = JOIST
        if mem1.PlaneAngleOfRotation == 90:
            p2.Point1 = P1 + BEAM.TranslateToGlobal((P0.x - P1.x), 0, -FACT*(AFSTDX - 1.5))
            p2.Point2 = p2.Point1 + (AFSTDY + (ROWS-1)*SPCY + PL_VED, 0,0)
        else:
            p2.Point1 = P1 + BEAM.TranslateToGlobal((P0.y - P1.y), 0, FACT*(AFSTDX -1.5))
            p2.Point2 = p2.Point1 + (AFSTDY + (ROWS-1)*SPCY + PL_VED, 0,0)
        p2.MaterialGrade = PL_GRD
        p2.MaterialOriginPoint = "Center"
        p2.TopOperationTypeLeftEnd = "None"
        p2.TopOperationTypeRightEnd = "None"
        p2.TopLengthLeft = BEAM.k - BEAM.tf
        p2.TopLengthRight =  BEAM.k - BEAM.tf
        p2.TopClipLeft = p2.TopLengthLeft
        p2.TopClipRight = p2.TopLengthRight
        p2.BottomOperationTypeLeftEnd = "None"
        p2.BottomOperationTypeLeftEnd = "None"
        p2.BottomLengthLeft = BEAM.k - BEAM.tf
        p2.BottomLengthRight = BEAM.k - BEAM.tf
        p2.BottomClipLeft = p2.TopLengthLeft
        p2.BottomClipRight = p2.TopLengthRight
        if PLJ_WIDTH >= AFSTDX + (COLS - 1)*SPCX + PL_HED: #TO ADD 6 INCHES OR NOT
            p2.Width = PLJ_WIDTH
        else:
            p2.Width = AFSTDX + (COLS - 1)*SPCX + PL_HED #TO ADD 6 INCHES OR NOT
        p2.Thickness = JWEB
        p2.WorkpointSlopeDistance = p2.Point1.Distance(p2.Point2)
        p2.MaterialSetbackLeftEnd = 0
        p2.MaterialSetbackRightEnd = 0
        if PL_EPF.count('Extend past flange') == 1:
            p2.MaterialSetbackLeftEnd = 0
            p2.MaterialSetbackRightEnd = 0
        else:
            p2.MaterialSetbackLeftEnd = BEAM.tf + 0.4375 #(AFSTDY - PL_VED)
            p2.MaterialSetbackRightEnd = 0
        p2.WebCutLeftEnd = 0
        p2.WebCutRightEnd = 0
        p2.OrderLength = p2.WorkpointSlopeDistance - p2.MaterialSetbackLeftEnd - p2.MaterialSetbackRightEnd
        p2.MaterialType = "Plate"
        p2.SurfaceFinish = "Red oxide"
        p2.MaterialColor3d = "Medium_material"
        p2.ReferencePointOffset = (0, 0, 0)
        p2.Add()
        p2.Rotate(p2.Member, (90 + FACT*90, 0, -90))
        #joist plate ends
        #match hole group add begins
        hole6 = Hole()
        hole6.Material = [p2, ]
        hole6.Holes = [hole3, ]
        hole6.Type = BH_TYP
        hole6.Matchable = 'Yes'
        hole6.ShouldBeValid = 'Yes'
        hole6.Diameter = hole3.calc_hole_size()
        hole6.BothSides = 'Yes'
        hole6.ShowWindow = 'Yes'
        hole6.Create()
        #match hole group add ends
        #bolt add to beam begins
        try:
            bolt2 = Bolt()
            bolt2.Material = [rl2, ]
            bolt2.Match = [BEAM.Material(0), ]
            bolt2.Diameter = hole4.BoltDiameter
            bolt2.PrimaryNutType = "Heavy hex"
            bolt2.SecondaryNutType = "None"
            bolt2.BoltType = BL_GRD
            bolt2.IsFieldBolt = "Shop"
            bolt2.IsTensionControl = "No"
            bolt2.Finish = "Black"
            bolt2.PrimaryHeadWasher.TypeDescription = "None"
            bolt2.PrimaryHeadWasher.GradeDescription = "F436"
            bolt2.PrimaryHeadWasher.Quantity = 0
            bolt2.PrimaryHeadWasher.Thickness = 0
            bolt2.PrimaryHeadWasher.Width = 0
            bolt2.PrimaryHeadWasher.Rotation = 0
            bolt2.SecondaryHeadWasher.TypeDescription = "None"
            bolt2.SecondaryHeadWasher.GradeDescription = "F436"
            bolt2.SecondaryHeadWasher.Quantity = 0
            bolt2.SecondaryHeadWasher.Thickness = 0
            bolt2.SecondaryHeadWasher.Width = 0
            bolt2.SecondaryHeadWasher.Rotation = 0
            bolt2.TertiaryHeadWasher.TypeDescription = "None"
            bolt2.TertiaryHeadWasher.GradeDescription = "F436"
            bolt2.TertiaryHeadWasher.Quantity = 0
            bolt2.TertiaryHeadWasher.Thickness = 0
            bolt2.TertiaryHeadWasher.Width = 0
            bolt2.TertiaryHeadWasher.Rotation = 0
            bolt2.PrimaryNutWasher.TypeDescription = "Hardened"
            bolt2.PrimaryNutWasher.GradeDescription = "F436"
            bolt2.PrimaryNutWasher.Quantity = 1
            bolt2.PrimaryNutWasher.Thickness = 4
            bolt2.PrimaryNutWasher.Width = 38
            bolt2.PrimaryNutWasher.Rotation = 0
            bolt2.SecondaryNutWasher.TypeDescription = "None"
            bolt2.SecondaryNutWasher.GradeDescription = "F436"
            bolt2.SecondaryNutWasher.Quantity = 0
            bolt2.SecondaryNutWasher.Thickness = 0
            bolt2.SecondaryNutWasher.Width = 0
            bolt2.SecondaryNutWasher.Rotation = 0
            bolt2.TertiaryNutWasher.TypeDescription = "None"
            bolt2.TertiaryNutWasher.GradeDescription = "F436"
            bolt2.TertiaryNutWasher.Quantity = 0
            bolt2.TertiaryNutWasher.Thickness = 0
            bolt2.TertiaryNutWasher.Width = 0
            bolt2.TertiaryNutWasher.Rotation = 0
            bolt2.ShowWindow = "No"
            bolt2.Direction = "Out"
            bolt2.AddMatch()
        except:
            pass
        #bolt add to beam ends
        #bolt add begins
        bolt3 = Bolt()
        bolt3.Material = [p2, ]
        bolt3.Match = [rl2, ]
        bolt3.Diameter = hole3.BoltDiameter
        bolt3.PrimaryNutType = "Heavy hex"
        bolt3.SecondaryNutType = "None"
        bolt3.BoltType = BL_GRD
        bolt3.IsFieldBolt = "Field"
        bolt3.IsTensionControl = "No"
        bolt3.Finish = "Black"
        bolt3.PrimaryHeadWasher.TypeDescription = "None"
        bolt3.PrimaryHeadWasher.GradeDescription = "F436"
        bolt3.PrimaryHeadWasher.Quantity = 0
        bolt3.PrimaryHeadWasher.Thickness = 0
        bolt3.PrimaryHeadWasher.Width = 0
        bolt3.PrimaryHeadWasher.Rotation = 0
        bolt3.SecondaryHeadWasher.TypeDescription = "None"
        bolt3.SecondaryHeadWasher.GradeDescription = "F436"
        bolt3.SecondaryHeadWasher.Quantity = 0
        bolt3.SecondaryHeadWasher.Thickness = 0
        bolt3.SecondaryHeadWasher.Width = 0
        bolt3.SecondaryHeadWasher.Rotation = 0
        bolt3.TertiaryHeadWasher.TypeDescription = "None"
        bolt3.TertiaryHeadWasher.GradeDescription = "F436"
        bolt3.TertiaryHeadWasher.Quantity = 0
        bolt3.TertiaryHeadWasher.Thickness = 0
        bolt3.TertiaryHeadWasher.Width = 0
        bolt3.TertiaryHeadWasher.Rotation = 0
        bolt3.PrimaryNutWasher.TypeDescription = "Hardened"
        bolt3.PrimaryNutWasher.GradeDescription = "F436"
        bolt3.PrimaryNutWasher.Quantity = 1
        bolt3.PrimaryNutWasher.Thickness = 4
        bolt3.PrimaryNutWasher.Width = 38
        bolt3.PrimaryNutWasher.Rotation = 0
        bolt3.SecondaryNutWasher.TypeDescription = "None"
        bolt3.SecondaryNutWasher.GradeDescription = "F436"
        bolt3.SecondaryNutWasher.Quantity = 0
        bolt3.SecondaryNutWasher.Thickness = 0
        bolt3.SecondaryNutWasher.Width = 0
        bolt3.SecondaryNutWasher.Rotation = 0
        bolt3.TertiaryNutWasher.TypeDescription = "None"
        bolt3.TertiaryNutWasher.GradeDescription = "F436"
        bolt3.TertiaryNutWasher.Quantity = 0
        bolt3.TertiaryNutWasher.Thickness = 0
        bolt3.TertiaryNutWasher.Width = 0
        bolt3.TertiaryNutWasher.Rotation = 0
        bolt3.ShowWindow = "No"
        bolt3.Direction = "Out"
        bolt3.AddMatch()
        #bolt add ends 
    
    #stiffener to add
    if PL_EPF.count('Stiffener opposite') == 1:
        p3 = RectPlate()
        p3.Member = BEAM
        if mem1.PlaneAngleOfRotation == 90:
            p3.Point1 = P1 + BEAM.TranslateToGlobal((P0.x - P1.x) - S_FACT*((JWEB + PL_THCK)*0.5), 0, FACT*BEAM.tw*0.5)
        else:
            p3.Point1 = P1 + BEAM.TranslateToGlobal((P0.y - P1.y) + S_FACT*((JWEB + PL_THCK)*0.5), 0, -FACT*BEAM.tw*0.5)
        p3.Point2 = p3.Point1 + (BEAM.depth, 0,0)
        p3.MaterialGrade = PL_GRD
        p3.MaterialOriginPoint = "Center"
        p3.TopOperationTypeLeftEnd = "Clip"
        p3.TopOperationTypeRightEnd = "Clip"
        p3.TopLengthLeft = BEAM.k - BEAM.tf
        p3.TopLengthRight =  BEAM.k - BEAM.tf
        p3.TopClipLeft = p3.TopLengthLeft
        p3.TopClipRight = p3.TopLengthRight
        p3.BottomOperationTypeLeftEnd = "None"
        p3.BottomOperationTypeRightEnd = "None"
        p3.BottomLengthLeft = 0
        p3.BottomLengthRight = 0
        p3.BottomCopeLeft = 0
        p3.BottomCopeRight = 0
        p3.Width = (BEAM.bf - BEAM.tw)*0.5
        p3.Thickness = PL_THCK
        p3.WorkpointSlopeDistance = p3.Point1.Distance(p3.Point2)
        p3.MaterialSetbackLeftEnd = BEAM.tf
        p3.MaterialSetbackRightEnd = BEAM.tf
        p3.WebCutLeftEnd = 0
        p3.WebCutRightEnd = 0
        p3.OrderLength = p3.WorkpointSlopeDistance - p3.MaterialSetbackLeftEnd - p3.MaterialSetbackRightEnd
        p3.MaterialType = "Plate"
        p3.SurfaceFinish = "Red oxide"
        p3.MaterialColor3d = "Medium_material"
        p3.ReferencePointOffset = (0, 0, 0)
        p3.Add()
        if mem1.PlaneAngleOfRotation == 90:
            p3.Rotate(BEAM, (-FACT*90, 0, -90))
        else:
            p3.Rotate(BEAM, (FACT*90, 0, -90))
        #weld add begin
        weld1 = Weld()
        weld1.Material = [p3, ]
        weld1.WeldTo = [BEAM, ]
        weld1.ArrowSize = WLD_SZE
        weld1.OtherSize = WLD_SZE
        weld1.FieldWeld = 'No'
        weld1.WeldAllAround = 'No'
        weld1.SpacerBarRequired = 'No'
        weld1.NonPrequalifiedWeld = 'Yes'
        weld1.JointType = 'None'
        weld1.Penetration = 'None'
        weld1.Process = 'None'
        weld1.Position = 'None'
        weld1.MaximumGap = 0
        weld1.WeldInside = 'No'
        weld1.one_weld_per_segment = 'No'
        weld1.min_length = p3.Thickness + 0.0625
        weld1.generate_fillet = 'No'
        weld1.generate_flare = 'No'
        weld1.generate_plug = 'No'
        weld1.generate_v_groove = 'No'
        weld1.generate_bevel_groove = 'No'
        weld1.ArrowWeldType = 'Fillet'
        weld1.ArrowLeftSetback = 0
        weld1.ArrowRightSetback = 0
        weld1.ArrowRootFace = 0
        weld1.ArrowRootOpening = 0
        weld1.arrow_effective_throat = 0
        weld1.ArrowWeldContourDescription = 'None'
        weld1.ArrowGrooveAngle = 0
        weld1.ArrowFilletBackupWeld = 'No'
        weld1.Stitch = 'No'
        weld1.ArrowStitchLength = 0
        weld1.ArrowStitchSpacing = 0
        weld1.ArrowLeftTermination = 0
        weld1.ArrowRightTermination = 0
        weld1.OtherWeldTypeIndex = 'Fillet'
        weld1.OtherLeftSetback = 0
        weld1.OtherRightSetback = 0
        weld1.OtherRootFace = 0
        weld1.OtherRootOpening = 0
        weld1.other_effective_throat = 0
        weld1.OtherContour = 'None'
        weld1.OtherGrooveAngle = 0
        weld1.OtherFilletBack = 'No'
        weld1.other_stitch = 'None'
        weld1.OtherStitchLength = 0
        weld1.OtherStitchSpacing = 0
        weld1.OtherLeftTermination = 0
        weld1.OtherRightTermination = 0
        weld1.WeldSymbolTailText = "TYP"
        weld1.ShowWindow = 'No'
        weld1.Create()
        #weld add end
#Function ends

while True:
    ClearSelection()
    try:
        mem_list = MultiMemberLocate("Select Joists")
    except:
        break
    
    # Dialog begin
    dlg1 = Dialog( "JOIST COMPOSITE SHEAR CONNEX V2019.1" )

    dlg1.tabset_begin()

    dlg1.tab("[ MAIN ]")
    dlg1.column_group_begin()

    dlg1.column(0)
    dlg1.group_title("LEFT END")            
    dlg1.checkbutton( 'chk_L', ('Connect?',), ('Connect?',), "" )
    dlg1.entry( 'set_L', 0.5, "Field clearance:")
    dlg1.menu('typ_cnx', ('Plate', 'Angle'), typ_cnx, "Type of Connection:")                 
    dlg1.menu('pl_grade', pl_gradeList, pl_grade, "Shear tab plate grade:")

    dlg1.column(0) #Col Start
    dlg1.group_title("RIGHT END")
    dlg1.checkbutton( 'chk_R', ('Connect?',), ('Connect?',), "" )
    dlg1.entry( 'set_R', 0.5, "Field clearance:")
    dlg1.menu('typ_cnx2', ('Plate', 'Angle'), typ_cnx2, "Type of Connection:")    
    dlg1.menu('pl_grade2', pl_gradeList, pl_grade2, "Shear tab grade:")

    dlg1.tab("[ PLATE ]")
    dlg1.column_group_begin()

    dlg1.column(0)

    dlg1.group_title("[ Connection Specifications ]")
    dlg1.checkbutton( 'chk_csL', ('Extend past flange', 'Stiffener opposite'), (), "" )

    dlg1.group_title("[ Beam Shear Tab ]")
    dlg1.entry( 'pl_thck', 0.5, "Thickness:")
    dlg1.menu('pl_side', ("NS", "FS"), pl_side, "Side:")
    dlg1.menu('ext_to', ext_toList, ext_to, "Extend size to:")
    dlg1.entry('dpth_hght', 6.0, "Depth or Height")
    dlg1.menu('top_cp', ("Yes", "No"), top_cp, "*Top cope:")
    dlg1.entry( 'top_cpd', 3.0, "*Length: >= H*J")
    dlg1.entry( 'top_cpl', 1.0, "*Depth:")
    dlg1.menu('btm_cp', ("Yes", "No"), btm_cp, "*Bottom cope:")
    dlg1.entry( 'btm_cpd', 3.0, "*Length: >= H*J")
    dlg1.entry( 'btm_cpl', 15.0, "*Depth:")

    dlg1.group_title("[ Bolt to suppported ]")
    dlg1.entry('bolt_dia', 0.75, "Diameter:")
    dlg1.menu('hole_type', hole_typeList, hole_type, "Hole type:")
    dlg1.menu('bolt_grade', bolt_gradeList, bolt_grade, "Grade:")
    dlg1.entry( 'bolt_rows', 3, "D)Rows: D*F < Beam Depth")
    dlg1.entry( 'bolt_fstdy', 3.0, "E)Vertical to 1st hole: > G")
    dlg1.entry( 'bolt_rspc', 3.0, "F)Vertical hole spacing: D*F < Beam Depth")
    dlg1.entry( 'bolt_vedist', 1.5, "G)Vertical edge distance: ***")
    dlg1.entry( 'bolt_cols', 1, "H)Columns:")
    dlg1.entry( 'bolt_fstdx', 1.5, "I)Horizontal to 1st hole:")
    dlg1.entry( 'bolt_cspc', 3.0, "J)Horizontal hole spacing: ")
    dlg1.entry( 'bolt_hedist', 1.5, "K)Horizontal edge distance: ***")

    dlg1.group_title("[ Weld ]")
    dlg1.label( "Fillet", "Weld Type:")
    dlg1.entry( 'weld_type', 0.25, "Weld Size:")

    dlg1.group_title("[ Joist Shear Tab ]")
    dlg1.checkbutton( 'chk_kL', ('Kicker Off',), ('Kicker Off',), "" )
    dlg1.label( "1", "Thickness:")
    dlg1.entry( 'jpl_width', 7.5, "PL min width: (K + (H-1)*J + 6)")

    dlg1.group_title_end() #Col Finish

    dlg1.column(0) #Col Start
    dlg1.image(image_file_path)
    dlg1.group_title_end() #Col Finish


    dlg1.column(0) #Col Start

    dlg1.group_title("[ Connection Specifications ]")
    dlg1.checkbutton( 'chk_csR', ('Extend past flange', 'Stiffener opposite'), (), "" )

    dlg1.group_title("[ Shear Tab ]")
    dlg1.entry( 'pl_thck2', 0.5, "Thickness:")
    dlg1.menu('pl_side2', ("NS", "FS"), pl_side2, "Side:")
    dlg1.menu('ext_to2', ext_toList, ext_to2, "Extend size to:")
    dlg1.entry('dpth_hght2', 6.0, "Depth or Height")
    dlg1.menu('top_cp2', ("Yes", "No"), top_cp, "*Top cope:")
    dlg1.entry( 'top_cpd2', 3.0, "*Length: >= H*J")
    dlg1.entry( 'top_cpl2', 1.0, "*Depth:")
    dlg1.menu('btm_cp2', ("Yes", "No"), btm_cp, "*Bottom cope:")
    dlg1.entry( 'btm_cpd2', 3.0, "*Length: >= H*J")
    dlg1.entry( 'btm_cpl2', 15.0, "*Depth:")


    dlg1.group_title("[ Bolt to supported ]")
    dlg1.entry('bolt_dia2', 0.75, "Diameter:")
    dlg1.menu('hole_type2', hole_typeList, hole_type2, "Hole type:")
    dlg1.menu('bolt_grade2', bolt_gradeList, bolt_grade2, "Grade:")
    dlg1.entry( 'bolt_rows2', 3, "D)Rows: D*F < Beam Depth")
    dlg1.entry( 'bolt_fstdy2', 3.0, "E)Vertical to 1st hole: > G")
    dlg1.entry( 'bolt_rspc2', 3.0, "F)Vertical hole spacing: D*F < Beam Depth")
    dlg1.entry( 'bolt_vedist2', 1.5, "G)Vertical edge distance: ***")
    dlg1.entry( 'bolt_cols2', 1, "H)Columns:")
    dlg1.entry( 'bolt_fstdx2', 1.5, "I)Horizontal to 1st hole:")
    dlg1.entry( 'bolt_cspc2', 3.0, "J)Horizontal hole spacing:")
    dlg1.entry( 'bolt_hedist2', 1.5, "K)Horizontal edge distance: ***")

    dlg1.group_title("[ Weld ]")
    dlg1.label( "Fillet", "Weld Type:")
    dlg1.entry( 'weld_type2', 0.25, "Weld Size:")

    dlg1.group_title("[ Joist Shear Tab ]")
    dlg1.checkbutton( 'chk_kR', ('Kicker Off',), ('Kicker Off',), "" )
    dlg1.label( "1", "Thickness:")
    dlg1.entry( 'jpl_width2', 7.5, "PL min width: (K + (H-1)*J + 6)")


    dlg1.group_title_end() #Col Finish



    dlg1.tab("[ ANGLE ]")
    dlg1.column_group_begin()

    dlg1.column(0)

    dlg1.group_title("[ Connection Specifications ]")
    dlg1.checkbutton( 'chk_csL', ('Extend past flange', 'Stiffener opposite'), (), "" )

    dlg1.group_title("[ Angle Specification ]")
    dlg1.mtrl_browse('ang_mtrl', ("Angle",), ang_mtrl, "Angle material:" )
    dlg1.menu('pl_side', ("NS", "FS"), pl_side, "Side:")

    dlg1.group_title("[ Bolt to suppported ]")
    dlg1.entry('bolt_dia', 0.75, "Diameter:")
    dlg1.menu('hole_type', hole_typeList, hole_type, "Hole type:")
    dlg1.menu('bolt_grade', bolt_gradeList, bolt_grade, "Grade:")
    dlg1.entry( 'bolt_rows', 3, "C)Rows:")
    dlg1.entry( 'abolt_fstdy', 3.0, "D)Vertical to 1st hole:")
    dlg1.entry( 'bolt_rspc', 3.0, "E)Vertical hole spacing:")
    dlg1.entry( 'bolt_vedist', 1.5, "G/F)Vertical edge distance: ***")
    dlg1.entry( 'bolt_cols', 1, "H)Columns:")
    dlg1.entry( 'abolt_fstdx', 3.75, "I)Horizontal to 1st hole:")
    dlg1.entry( 'bolt_cspc', 3.0, "J)Horizontal hole spacing: ")
    #dlg1.entry( 'bolt_hedist', 1.5, "K)Horizontal edge distance: ***")

    dlg1.group_title("[ Bolt to supporting ]")
    dlg1.entry('bolt_dias', 0.75, "Diameter:")
    dlg1.menu('hole_types', hole_typeList, hole_type, "Hole type:")
    dlg1.menu('bolt_grades', bolt_gradeList, bolt_grade, "Grade:")
    dlg1.entry( 'bolt_rowss', 3, "K)Rows:")
    dlg1.entry( 'abolt_fstdys', 3.0, "L)Vertical to 1st hole:")
    dlg1.entry( 'bolt_rspcs', 3.0, "M)Vertical hole spacing:")
    dlg1.entry( 'bolt_vedists', 1.5, "O/N)Vertical edge distance: ***")
    dlg1.entry( 'bolt_colss', 1, "P)Columns:")
    dlg1.entry( 'abolt_fstdxs', 2.25, "Q)Horizontal to 1st hole:")
    dlg1.entry( 'bolt_cspcs', 3.0, "R)Horizontal hole spacing: ")
    #dlg1.entry( 'bolt_hedist', 1.5, "K)Horizontal edge distance: ***")

    dlg1.group_title("[ Joist Shear Tab ]")
    dlg1.label( "1", "Thickness:")
    dlg1.entry( 'jpl_width', 7.5, "PL min width: (K + (H-1)*J + 6)")

    dlg1.group_title_end() #Col Finish

    dlg1.column(0) #Col Start
    dlg1.image(image_file_path2)
    dlg1.group_title_end() #Col Finish


    dlg1.column(0) #Col Start

    dlg1.group_title("[ Connection Specifications ]")
    dlg1.checkbutton( 'chk_csR', ('Extend past flange', 'Stiffener opposite'), (), "" )

    dlg1.group_title("[ Angle Specification ]")
    #dlg1.choosemtrl('ang_sct', ("Angle", ), ang_sct, "Angle Section:")
    dlg1.mtrl_browse('ang_mtrl2', ("Angle",), ang_mtrl2, "Angle material:" )
    dlg1.menu('pl_side2', ("NS", "FS"), pl_side2, "Side:")

    dlg1.group_title("[ Bolt to supported ]")
    dlg1.entry('bolt_dia2', 0.75, "Diameter:")
    dlg1.menu('hole_type2', hole_typeList, hole_type, "Hole type:")
    dlg1.menu('bolt_grade2', bolt_gradeList, bolt_grade, "Grade:")
    dlg1.entry( 'bolt_rows2', 3, "C)Rows:")
    dlg1.entry( 'abolt_fstdy2', 3.0, "D)Vertical to 1st hole: > G")
    dlg1.entry( 'bolt_rspc2', 3.0, "E)Vertical hole spacing: D*F < Beam Depth")
    dlg1.entry( 'bolt_vedist2', 1.5, "G/F)Vertical edge distance: ***")
    dlg1.entry( 'bolt_cols2', 1, "H)Columns:")
    dlg1.entry( 'abolt_fstdx2', 3.75, "I)Horizontal to 1st hole:")
    dlg1.entry( 'bolt_cspc2', 3.0, "J)Horizontal hole spacing:")
    #dlg1.entry( 'bolt_hedist2', 1.5, "K)Horizontal edge distance: ***")

    dlg1.group_title("[ Bolt to supporting ]")
    dlg1.entry('bolt_dia2s', 0.75, "Diameter:")
    dlg1.menu('hole_type2s', hole_typeList, hole_type, "Hole type:")
    dlg1.menu('bolt_grade2s', bolt_gradeList, bolt_grade, "Grade:")
    dlg1.entry( 'bolt_rows2s', 3, "K)Rows: D*F < Beam Depth")
    dlg1.entry( 'abolt_fstdy2s', 3.0, "L)Vertical to 1st hole: > G")
    dlg1.entry( 'bolt_rspc2s', 3.0, "M)Vertical hole spacing: D*F < Beam Depth")
    dlg1.entry( 'bolt_vedist2s', 1.5, " O/N)Vertical edge distance: ***")
    dlg1.entry( 'bolt_cols2s', 1, "P)Columns:")
    dlg1.entry( 'abolt_fstdx2s', 2.25, "Q)Horizontal to 1st hole:")
    dlg1.entry( 'bolt_cspc2s', 3.0, "R)Horizontal hole spacing:")
    #dlg1.entry( 'bolt_hedist2s', 1.5, "K)Horizontal edge distance: ***")

    dlg1.group_title("[ Joist Shear Tab ]")
    dlg1.label( "1", "Thickness:")
    dlg1.entry( 'jpl_width2', 7.5, "PL min width: (K + (H-1)*J + 6)")


    dlg1.group_title_end() #Col Finish

    try:
        dd = dlg1.done()
    except ResponseNotOK:
        break


    globals().update(dd)
   
    #Selection Begins
    #mem1 = MemberLocate("Select Joist")
    for mem1 in mem_list:
        pt1 = mem1.LeftEnd.Location
        pt2 = mem1.RightEnd.Location
        mem1mt = mem1.Material(0)

        #To know framing members at both ends of selected member
        for sup_ldx in mem1.LeftEnd.Nodes:
            if sup_ldx == 0:
                continue
            mem2 = Member(sup_ldx)
            pt21 = mem2.LeftEnd.Location
            pt22 = mem2.RightEnd.Location
        for sup_idx in mem1.RightEnd.Nodes:
            if sup_idx == 0:
                continue
            mem3 = Member(sup_idx)
            pt31 = mem3.LeftEnd.Location
            pt32 = mem3.RightEnd.Location
        #To know framing members at both ends of selected member



        #Plate side
        if pl_side == "NS":
            st_s1 = -1
        else:
            st_s1 = 1

        if pl_side2 == "NS":
            st_s2 = -1
        else:
            st_s2 = 1
        #Plate side

        #CJ_SHEARTAB (BEAM, P0, P1, JOIST, JWEB,            PL_THCK, PL_EXT2, PL_EPF, PL_TC, PL_TCL, PL_TCD, PL_BC, PL_BCL, PL_BCD, FL_CLR, PL_HED,         PL_GRD, S_FACT, FSTDX, FSTDY, DIAM, BH_TYP, BL_GRD, COLS, ROWS, SPCX, SPCY,                              FACT)
        #CJ_SHEARTAB (BEAM, P0, P1, JOIST, JWEB, PLJ_WIDTH, PL_THCK, PL_EXT2, PL_EPF, PL_TC, PL_TCL, PL_TCD, PL_BC, PL_BCL, PL_BCD, FL_CLR, PL_HED, PL_VED, PL_GRD, S_FACT, FSTDX, FSTDY, DIAM, BH_TYP, BL_GRD, COLS, ROWS, SPCX, SPCY, WLD_SZE, PL_ANGL, ANGL_,MAT, FACT)
                
        CJ_SHEARTAB (mem2, pt1, pt21, mem1, 1, jpl_width, pl_thck, ext_to, dpth_hght, chk_kL, chk_csL, top_cp, top_cpl, top_cpd, btm_cp, btm_cpl, btm_cpd, set_L, bolt_hedist, bolt_vedist, pl_grade, st_s1, bolt_fstdx, bolt_fstdy, abolt_fstdx, abolt_fstdy, abolt_fstdxs, abolt_fstdys, bolt_dia, bolt_dias, hole_type, bolt_grade, bolt_cols, bolt_rows, bolt_colss, bolt_rowss, bolt_rspc, bolt_cspc, bolt_rspcs, bolt_cspcs, weld_type, typ_cnx, ang_mtrl, 1)
        CJ_SHEARTAB (mem3, pt1, pt31, mem1, 1, jpl_width2, pl_thck2, ext_to2, dpth_hght2, chk_kR, chk_csR, top_cp2, top_cpl2, top_cpd2, btm_cp2, btm_cpl, btm_cpd, set_R, bolt_hedist2, bolt_vedist2, pl_grade2, st_s2, bolt_fstdx2, bolt_fstdy2, abolt_fstdx2, abolt_fstdy2, abolt_fstdx2s, abolt_fstdy2s, bolt_dia2, bolt_dia2s, hole_type2, bolt_grade2, bolt_cols2, bolt_rows2, bolt_cols2s, bolt_rows2s, bolt_rspc2, bolt_cspc2, bolt_rspc2s, bolt_cspc2s, weld_type2, typ_cnx2, ang_mtrl2, -1)

    ClearSelection()
    if not yes_or_no('Select others joist?'):
        break


