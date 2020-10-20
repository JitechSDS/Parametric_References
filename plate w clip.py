# startup code begin
from param import *
from math import *
Units("feet")
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
# rectangular plate begin
p1 = RectPlate()
p1.Member = MemberLocate('Select Member to add mtrl to')
p1.Point1 = p1.Member.LeftEnd.Location + p1.Member.TranslateToGlobal( -1434.141317, -42.23, 0.515 )
p1.Point2 = p1.Point1 + p1.Member.TranslateToGlobal( 0, 0, 7.425989 )
p1.MaterialGrade = 'A36'
p1.MaterialOriginPoint = 'FS'
p1.TopOperationTypeLeftEnd = 'None'
p1.TopOperationTypeRightEnd = 'None'
p1.BottomOperationTypeLeftEnd = 'Clip'
p1.BottomOperationTypeRightEnd = 'None'
p1.BottomLengthLeft = 1.25
p1.BottomClipLeft = 1.25
p1.Width = 0.75
p1.Thickness = 0.25
p1.WorkpointSlopeDistance = p1.Point1.Distance(p1.Point2)
p1.MaterialSetbackLeftEnd = 0
p1.MaterialSetbackRightEnd = 0
p1.WebCutLeftEnd = 0
p1.WebCutRightEnd = 0
p1.OrderLength = p1.WorkpointSlopeDistance - p1.MaterialSetbackLeftEnd - p1.MaterialSetbackRightEnd
p1.MaterialType = 'Plate'
p1.SurfaceFinish = 'Red oxide'
p1.MaterialColor3d = 'Medium_beam'
p1.ReferencePointOffset = (0, 0, 0)
p1.Add()
p1.Rotate(p1.Member, (0.000000, 90.000000, 0.000000))
# rectangular plate end
# rolled section begin
rl4 = RolledSection()
rl4.Member = p1.member
rl4.Point1 = p1.left.location
rl4.Point2 = p1.left.location
rl4.MaterialGrade = 'A992'
rl4.Centered = 'No'
rl4.TopOperationTypeLeftEnd = 'Cope plain'
rl4.TopOperationTypeRightEnd = 'None'
rl4.TopLengthLeft = 8
rl4.TopCopeLeft = 2
rl4.BottomOperationTypeLeftEnd = 'None'
rl4.BottomOperationTypeRightEnd = 'None'
rl4.IsLongLegVerticalMaterial = 'VT.'
rl4.ToeInOrOut = 'Out'
rl4.RollType = 'None'
rl4.FieldWeldPrepFlagLeftEnd = 'No'
rl4.FieldWeldPrepFlagRightEnd = 'No'
rl4.MomentConnectionWebSetbackLeftEnd = 0
rl4.MomentConnectionWebSetbackRightEnd = 0
rl4.MaterialTwistAngle = 0
rl4.MidOrdinate = 0
rl4.IncludedAngle = 0
rl4.RollingRadius = 0
rl4.SpiralOffset = 0
rl4.WorkpointSlopeDistance = rl4.Point1.Distance(rl4.Point2)
rl4.MaterialSetbackLeftEnd = 0
rl4.MaterialSetbackRightEnd = 0
rl4.WebCutLeftEnd = 0
rl4.WebCutRightEnd = 0
rl4.FlangeCutLeftEnd = 0
rl4.FlangeCutRightEnd = 0
rl4.LeftEndPreparation = 'Standard cut'
rl4.RightEndPreparation = 'Standard cut'
rl4.OrderLength = rl4.WorkpointSlopeDistance - rl4.MaterialSetbackLeftEnd - rl4.MaterialSetbackRightEnd
rl4.MaterialType = 'W flange'
rl4.SurfaceFinish = 'Red oxide'
rl4.MaterialColor3d = 'Medium_beam'
rl4.ReferencePointOffset = (0, 0, 0)
rl4.Add()
# rolled section end
