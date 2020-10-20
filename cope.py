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
# rolled section begin
rl3 = RolledSection()
rl3.Member = MemberLocate('Select Member to add mtrl to')
rl3.Point1 = rl3.Member.LeftEnd.Location + rl3.Member.TranslateToGlobal( 0, 0, 0.75 )
rl3.Point2 = rl3.Point1 + rl3.Member.TranslateToGlobal( 0, 0, 62.001071 )
rl3.SectionSize = 'L8x4x1/2'
rl3.MaterialGrade = 'A36'
rl3.Centered = 'No'
rl3.TopOperationTypeLeftEnd = 'None'
rl3.TopOperationTypeRightEnd = 'Cope plain'
rl3.TopLengthRight = 8
rl3.TopCopeRight = 2
rl3.BottomOperationTypeLeftEnd = 'None'
rl3.BottomOperationTypeRightEnd = 'None'
rl3.IsLongLegVerticalMaterial = 'VT.'
rl3.ToeInOrOut = 'Out'
rl3.RollType = 'None'
rl3.FieldWeldPrepFlagLeftEnd = 'No'
rl3.FieldWeldPrepFlagRightEnd = 'No'
rl3.MomentConnectionWebSetbackLeftEnd = 0
rl3.MomentConnectionWebSetbackRightEnd = 0
rl3.MaterialTwistAngle = 0
rl3.MidOrdinate = 0
rl3.IncludedAngle = 0
rl3.RollingRadius = 0
rl3.SpiralOffset = 0
rl3.WorkpointSlopeDistance = rl3.Point1.Distance(rl3.Point2)
rl3.MaterialSetbackLeftEnd = 0
rl3.MaterialSetbackRightEnd = 0
rl3.WebCutLeftEnd = 0
rl3.WebCutRightEnd = 0
rl3.FlangeCutLeftEnd = 0
rl3.FlangeCutRightEnd = 0
rl3.LeftEndPreparation = 'Standard cut'
rl3.RightEndPreparation = 'Standard cut'
rl3.OrderLength = rl3.WorkpointSlopeDistance - rl3.MaterialSetbackLeftEnd - rl3.MaterialSetbackRightEnd
rl3.MaterialType = 'Angle'
rl3.SurfaceFinish = 'Red oxide'
rl3.MaterialColor3d = 'Medium_beam'
rl3.ReferencePointOffset = (0, 0, 0)
rl3.Add()
rl3.Rotate(rl3.Member, (0.000000, 90.000000, 0.000000))
# rolled section end
