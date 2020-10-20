# startup code begin
from param import *
from math import *
Units("inch")
saved_sds2_version = '2018.19'
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
# rolled section begin
a36 = RolledSection()
a36.Member = a34.member
a36.Point1 = a36.Member.LeftEnd.Location + a36.Member.TranslateToGlobal( 0, -41.375, 0.515 )
a36.Point2 = a36.Point1 + a36.Member.TranslateToGlobal( 0, 5.465466, 0 )
a36.SectionSize = 'L5x5x1/2'
a36.MaterialGrade = 'A36'
a36.Centered = 'No'
a36.TopOperationTypeLeftEnd = 'None'
a36.TopOperationTypeRightEnd = 'None'
a36.BottomOperationTypeLeftEnd = 'None'
a36.BottomOperationTypeRightEnd = 'None'
a36.IsLongLegVerticalMaterial = 'VT.'
a36.ToeInOrOut = 'In'
a36.RollType = 'None'
a36.FieldWeldPrepFlagLeftEnd = 'No'
a36.FieldWeldPrepFlagRightEnd = 'No'
a36.MomentConnectionWebSetbackLeftEnd = 0
a36.MomentConnectionWebSetbackRightEnd = 0
a36.MaterialTwistAngle = 0
a36.MidOrdinate = 0
a36.IncludedAngle = 0
a36.RollingRadius = 0
a36.SpiralOffset = 0
a36.WorkpointSlopeDistance = a36.Point1.Distance(a36.Point2)
a36.MaterialSetbackLeftEnd = 0
a36.MaterialSetbackRightEnd = 0
a36.WebCutLeftEnd = 0
a36.WebCutRightEnd = 0
a36.FlangeCutLeftEnd = 0
a36.FlangeCutRightEnd = 0
a36.LeftEndPreparation = 'Standard cut'
a36.RightEndPreparation = 'Standard cut'
a36.OrderLength = a36.WorkpointSlopeDistance - a36.MaterialSetbackLeftEnd - a36.MaterialSetbackRightEnd
a36.MaterialType = 'Angle'
a36.SurfaceFinish = 'Red oxide'
a36.MaterialColor3d = 'Medium_beam'
a36.ReferencePointOffset = (0, 0, 0)
a36.Add()
a36.Rotate(a36.Member, (0.000000, 0.000000, 90.000000))
# rolled section end
# hole group add begin
hole47 = Hole()
hole47.Material = [a36, ]
hole47.Point = hole47.Material.Location + hole47.Material.TranslateToGlobal( 4.465466, -3.75, 0.5 )
hole47.Type = 'Standard Round'
hole47.Matchable = 'Yes'
hole47.ShouldBeValid = 'Yes'
hole47.ReferenceOffsetX = 0
hole47.ReferenceOffsetY = 0
hole47.SpacingX = 3
hole47.SpacingY = 3
hole47.GroupRotation = 0
hole47.Locate = 'Center'
hole47.Columns = 2
hole47.Rows = 1
hole47.BoltType = 'AUTO'
hole47.PlugType = 'No Plug'
hole47.BoltDiameter = 0.75
hole47.Diameter = hole47.CalculateHoleSize()
hole47.BothSides = 'Yes'
hole47.ShowWindow = 'Yes'
hole47.Create()
# hole group add end
# hole group add begin
hole49 = Hole()
hole49.Material = [a36.member, ]
hole49.Holes = [hole47, ]
hole49.Type = 'Standard Round'
hole49.Matchable = 'Yes'
hole49.ShouldBeValid = 'Yes'
hole49.Diameter = hole49.calc_hole_size()
hole49.BothSides = 'Yes'
hole49.ShowWindow = 'Yes'
hole49.Create()
# hole group add end
# hole group add begin
hole52 = Hole()
hole52.Material = [a36, ]
hole52.Point = hole52.Material.Location + hole52.Material.TranslateToGlobal( 2.965466, 0, 2.5 )
hole52.Type = 'Standard Round'
hole52.Matchable = 'Yes'
hole52.ShouldBeValid = 'Yes'
hole52.ReferenceOffsetX = 0
hole52.ReferenceOffsetY = 0
hole52.SpacingX = 3
hole52.SpacingY = 3
hole52.GroupRotation = 0
hole52.Locate = 'Center'
hole52.Columns = 1
hole52.Rows = 1
hole52.BoltType = 'AUTO'
hole52.PlugType = 'No Plug'
hole52.BoltDiameter = 0.75
hole52.Diameter = hole52.CalculateHoleSize()
hole52.BothSides = 'Yes'
hole52.ShowWindow = 'Yes'
hole52.Create()
# hole group add end
