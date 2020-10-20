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
# hole group add begin
hole1 = Hole()
hole1.Material = MtrlLocate('Locate material')
hole1.Point = hole1.Material.Location + hole1.Material.TranslateToGlobal( 234, -3.75, 0 )
hole1.Type = 'Standard Round'
hole1.Matchable = 'Yes'
hole1.MaterialFace = 'Web FS'
hole1.ShouldBeValid = 'Yes'
hole1.ReferenceOffsetX = 0
hole1.ReferenceOffsetY = 0
hole1.SpacingX = 3
hole1.SpacingY = 3
hole1.GroupRotation = 0
hole1.Locate = 'Center'
hole1.Columns = 1
hole1.Rows = 1
hole1.BoltType = 'AUTO'
hole1.PlugType = 'No Plug'
hole1.BoltDiameter = 0.75
hole1.Diameter = hole1.CalculateHoleSize()
hole1.BothSides = 'Yes'
hole1.ShowWindow = 'Yes'
hole1.Create()
# hole group add end
# rolled section begin
hss1 = RolledSection()
hss1.Member = MemberLocate('Select Member to add mtrl to')
hss1.Point1 = hss1.Member.LeftEnd.Location + hss1.Member.TranslateToGlobal( 240, 0, 6.8 )
hss1.Point2 = hss1.Point1 + hss1.Member.TranslateToGlobal( 0.101884, 0, -6.076219 )
hss1.SectionSize = 'L4x4x1/2'
hss1.MaterialGrade = 'A36'
hss1.Centered = 'No'
hss1.TopOperationTypeLeftEnd = 'None'
hss1.TopOperationTypeRightEnd = 'None'
hss1.BottomOperationTypeLeftEnd = 'None'
hss1.BottomOperationTypeRightEnd = 'None'
hss1.IsLongLegVerticalMaterial = 'VT.'
hss1.ToeInOrOut = 'Out'
hss1.RollType = 'None'
hss1.FieldWeldPrepFlagLeftEnd = 'No'
hss1.FieldWeldPrepFlagRightEnd = 'No'
hss1.MomentConnectionWebSetbackLeftEnd = 0
hss1.MomentConnectionWebSetbackRightEnd = 0
hss1.MaterialTwistAngle = 0
hss1.MidOrdinate = 0
hss1.IncludedAngle = 0
hss1.RollingRadius = 0
hss1.SpiralOffset = 0
hss1.WorkpointSlopeDistance = hss1.Point1.Distance(hss1.Point2)
hss1.MaterialSetbackLeftEnd = 0
hss1.MaterialSetbackRightEnd = 0
hss1.WebCutLeftEnd = 0
hss1.WebCutRightEnd = 0
hss1.FlangeCutLeftEnd = 0
hss1.FlangeCutRightEnd = 0
hss1.LeftEndPreparation = 'Standard cut'
hss1.RightEndPreparation = 'Standard cut'
hss1.OrderLength = hss1.WorkpointSlopeDistance - hss1.MaterialSetbackLeftEnd - hss1.MaterialSetbackRightEnd
hss1.MaterialType = 'Angle'
hss1.SurfaceFinish = 'Red oxide'
hss1.MaterialColor3d = 'Medium_beam'
hss1.ReferencePointOffset = (0, 0, 0)
hss1.Add()
hss1.Rotate(hss1.Member, (0.000000, -89.039374, 0.000000))
# rolled section end
# hole group add begin
hole3 = Hole()
hole3.Material = [hss1, ]
hole3.Holes = HoleLocate('Locate holes to match')
hole3.Type = 'Standard Round'
hole3.Matchable = 'Yes'
hole3.ShouldBeValid = 'Yes'
hole3.Diameter = hole3.calc_hole_size()
hole3.BothSides = 'Yes'
hole3.ShowWindow = 'Yes'
hole3.Create()
# hole group add end
# bolt add begin
bolt1 = Bolt()
bolt1.Material = [hss1.member, ]
bolt1.Match = [hss1, ]
bolt1.Diameter = 0.75
bolt1.PrimaryNutType = 'Heavy hex'
bolt1.SecondaryNutType = 'None'
bolt1.BoltType = 'AUTO'
bolt1.IsFieldBolt = 'Field'
bolt1.IsTensionControl = 'No'
bolt1.Finish = 'Black'
bolt1.ShowWindow = 'No'
bolt1.Direction = 'Out'
bolt1.AddMatch()
# bolt add end
