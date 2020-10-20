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
# rolled section begin
a38 = RolledSection()
a38.Member = MemberLocate('Select Member to add mtrl to')
a38.Point1 = a38.Member.LeftEnd.Location + a38.Member.TranslateToGlobal( 240, 0, 0.75 )
a38.Point2 = a38.Point1 + a38.Member.TranslateToGlobal( 0, 0, 5.79006 )
a38.SectionSize = 'L5x5x7/8'
a38.MaterialGrade = 'A36'
a38.Centered = 'No'
a38.TopOperationTypeLeftEnd = 'None'
a38.TopOperationTypeRightEnd = 'None'
a38.BottomOperationTypeLeftEnd = 'None'
a38.BottomOperationTypeRightEnd = 'None'
a38.IsLongLegVerticalMaterial = 'VT.'
a38.ToeInOrOut = 'In'
a38.RollType = 'None'
a38.FieldWeldPrepFlagLeftEnd = 'No'
a38.FieldWeldPrepFlagRightEnd = 'No'
a38.MomentConnectionWebSetbackLeftEnd = 0
a38.MomentConnectionWebSetbackRightEnd = 0
a38.MaterialTwistAngle = 0
a38.MidOrdinate = 0
a38.IncludedAngle = 0
a38.RollingRadius = 0
a38.SpiralOffset = 0
a38.WorkpointSlopeDistance = a38.Point1.Distance(a38.Point2)
a38.MaterialSetbackLeftEnd = 0
a38.MaterialSetbackRightEnd = 0
a38.WebCutLeftEnd = 0
a38.WebCutRightEnd = 0
a38.FlangeCutLeftEnd = 0
a38.FlangeCutRightEnd = 0
a38.LeftEndPreparation = 'Standard cut'
a38.RightEndPreparation = 'Standard cut'
a38.OrderLength = a38.WorkpointSlopeDistance - a38.MaterialSetbackLeftEnd - a38.MaterialSetbackRightEnd
a38.MaterialType = 'Angle'
a38.SurfaceFinish = 'Red oxide'
a38.MaterialColor3d = 'Medium_beam'
a38.ReferencePointOffset = (0, 0, 0)
a38.Add()
a38.Rotate(a38.Member, (-90.000000, 90.000000, 0.000000))
# rolled section end
# hole group add begin
hole54 = Hole()
hole54.Material = [a38, ]
hole54.Point = hole54.Material.Location + hole54.Material.TranslateToGlobal( 1, -3.75, -0.5 )
hole54.Type = 'Standard Round'
hole54.Matchable = 'Yes'
hole54.ShouldBeValid = 'Yes'
hole54.ReferenceOffsetX = 0
hole54.ReferenceOffsetY = 0
hole54.SpacingX = 3
hole54.SpacingY = 3
hole54.GroupRotation = 0
hole54.Locate = 'Center'
hole54.Columns = 2
hole54.Rows = 1
hole54.BoltType = 'AUTO'
hole54.PlugType = 'No Plug'
hole54.BoltDiameter = 0.75
hole54.Diameter = hole54.CalculateHoleSize()
hole54.BothSides = 'Yes'
hole54.ShowWindow = 'Yes'
hole54.Create()
# hole group add end
# hole group add begin
hole56 = Hole()
hole56.Material = [a38.member, ]
hole56.Holes = [hole54, ]
hole56.Type = 'Standard Round'
hole56.Matchable = 'Yes'
hole56.ShouldBeValid = 'Yes'
hole56.Diameter = hole56.calc_hole_size()
hole56.BothSides = 'Yes'
hole56.ShowWindow = 'Yes'
hole56.Create()
# hole group add end
# hole group add begin
hole64 = Hole()
hole64.Material = [a38, ]
hole64.Point = hole64.Material.Location + hole64.Material.TranslateToGlobal( 2.5, 0, -2.5 )
hole64.Type = 'Standard Round'
hole64.Matchable = 'Yes'
hole64.ShouldBeValid = 'Yes'
hole64.ReferenceOffsetX = 0
hole64.ReferenceOffsetY = 0
hole64.SpacingX = 3
hole64.SpacingY = 3
hole64.GroupRotation = 0
hole64.Locate = 'Center'
hole64.Columns = 1
hole64.Rows = 1
hole64.BoltType = 'AUTO'
hole64.PlugType = 'No Plug'
hole64.BoltDiameter = 0.75
hole64.Diameter = hole64.CalculateHoleSize()
hole64.BothSides = 'Yes'
hole64.ShowWindow = 'Yes'
hole64.Create()
# hole group add end
# bolt add begin
bolt1 = Bolt()
bolt1.Material = [a36, ]
bolt1.Match = [a36.member, ]
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
# bolt add begin
bolt2 = Bolt()
bolt2.Material = [a38, ]
bolt2.Match = [a38.member, ]
bolt2.Diameter = 0.75
bolt2.PrimaryNutType = 'Heavy hex'
bolt2.SecondaryNutType = 'None'
bolt2.BoltType = 'AUTO'
bolt2.IsFieldBolt = 'Field'
bolt2.IsTensionControl = 'No'
bolt2.Finish = 'Black'
bolt2.ShowWindow = 'No'
bolt2.Direction = 'Out'
bolt2.AddMatch()
# bolt add end
# rolled section begin
a44 = RolledSection()
a44.Member = a36.member
a44.Point1 = a44.Member.LeftEnd.Location + a44.Member.TranslateToGlobal( 22.158962, -38.409534, 0.515 )
a44.Point2 = a44.Point1 + a44.Member.TranslateToGlobal( 0, 38.409534, 10.985 )
a44.SectionSize = 'L5x5x1/2'
a44.MaterialGrade = 'A36'
a44.Centered = 'No'
a44.TopOperationTypeLeftEnd = 'None'
a44.TopOperationTypeRightEnd = 'None'
a44.BottomOperationTypeLeftEnd = 'None'
a44.BottomOperationTypeRightEnd = 'None'
a44.IsLongLegVerticalMaterial = 'VT.'
a44.ToeInOrOut = 'In'
a44.RollType = 'None'
a44.FieldWeldPrepFlagLeftEnd = 'No'
a44.FieldWeldPrepFlagRightEnd = 'No'
a44.MomentConnectionWebSetbackLeftEnd = 0
a44.MomentConnectionWebSetbackRightEnd = 0
a44.MaterialTwistAngle = 0
a44.MidOrdinate = 0
a44.IncludedAngle = 0
a44.RollingRadius = 0
a44.SpiralOffset = 0
a44.WorkpointSlopeDistance = a44.Point1.Distance(a44.Point2)
a44.MaterialSetbackLeftEnd = 0
a44.MaterialSetbackRightEnd = 0
a44.WebCutLeftEnd = 0
a44.WebCutRightEnd = 0
a44.FlangeCutLeftEnd = 0
a44.FlangeCutRightEnd = 0
a44.LeftEndPreparation = 'Standard cut'
a44.RightEndPreparation = 'Standard cut'
a44.OrderLength = a44.WorkpointSlopeDistance - a44.MaterialSetbackLeftEnd - a44.MaterialSetbackRightEnd
a44.MaterialType = 'Angle'
a44.SurfaceFinish = 'Red oxide'
a44.MaterialColor3d = 'Medium_beam'
a44.ReferencePointOffset = (0, 0, 0)
a44.Add()
a44.Rotate(a44.Member, (-90.000000, 15.960355, 90.000000))
# rolled section end
# hole group add begin
hole69 = Hole()
hole69.Material = [a44, ]
hole69.Holes = HoleLocate('Locate holes to match')
hole69.Type = 'Standard Round'
hole69.Matchable = 'Yes'
hole69.ShouldBeValid = 'Yes'
hole69.Diameter = hole69.calc_hole_size()
hole69.BothSides = 'Yes'
hole69.ShowWindow = 'Yes'
hole69.Create()
# hole group add end
# bolt add begin
bolt6 = Bolt()
bolt6.Material = [a44, ]
bolt6.Match = [a36, a38, ]
bolt6.Diameter = 0.75
bolt6.PrimaryNutType = 'Heavy hex'
bolt6.SecondaryNutType = 'None'
bolt6.BoltType = 'AUTO'
bolt6.IsFieldBolt = 'Field'
bolt6.IsTensionControl = 'No'
bolt6.Finish = 'Black'
bolt6.ShowWindow = 'No'
bolt6.Direction = 'Out'
bolt6.AddMatch()
# bolt add end
