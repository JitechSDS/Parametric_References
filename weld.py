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
# weld add begin
weld1 = Weld()
weld1.Material = MtrlLocate('Locate material to weld')
weld1.WeldTo = MtrlLocate('Locate material to weld to')
weld1.ArrowSize = 0.000000
weld1.OtherSize = 0.000000
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
weld1.min_length = 0
weld1.generate_fillet = 'No'
weld1.generate_flare = 'No'
weld1.generate_plug = 'No'
weld1.generate_v_groove = 'No'
weld1.generate_bevel_groove = 'No'
weld1.ArrowWeldType = 'None'
weld1.ArrowLeftSetback = 0
weld1.ArrowRightSetback = 0
weld1.ArrowRootFace = 0
weld1.ArrowRootOpening = 0
weld1.arrow_effective_throat = 0
weld1.ArrowWeldContourDescription = 'None'
weld1.ArrowGrooveAngle = 0
weld1.ArrowFilletBackupWeld = 'Yes'
weld1.Stitch = 'No'
weld1.ArrowStitchLength = 0
weld1.ArrowStitchSpacing = 0
weld1.ArrowLeftTermination = 0
weld1.ArrowRightTermination = 0
weld1.OtherWeldTypeIndex = 'None'
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
weld1.WeldSymbolTailText = ""
weld1.ShowWindow = 'No'
weld1.Create()
# weld add end
