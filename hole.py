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
# hole group add begin
hole1 = Hole()
hole1.Material = MtrlLocate('Locate material')
hole1.Point = hole1.Material.Location + hole1.Material.TranslateToGlobal( 88.106314, -4.548888, 0.1275 )
hole1.Type = 'Standard round'
hole1.Matchable = 'Yes'
hole1.MaterialFace = 'Web NS'
hole1.ShouldBeValid = 'Yes'
hole1.ReferenceOffsetX = 0
hole1.ReferenceOffsetY = 0
hole1.SpacingX = 3
hole1.SpacingY = 3
hole1.GroupRotation = 0
hole1.Locate = 'Center'
hole1.Columns = 2
hole1.Rows = 2
hole1.BoltType = 'AUTO'
hole1.PlugType = 'No Plug'
hole1.BoltDiameter = 0.75
hole1.Diameter = hole1.CalculateHoleSize()
hole1.BothSides = 'Yes'
hole1.ShowWindow = 'Yes'
hole1.Create()
# hole group add end
