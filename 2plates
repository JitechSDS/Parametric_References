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
    import rect_plate
    import hole_add
    import bolt_add
    
    def add_rect_plate(thickness, width, p1, p2, origin, member_number, subm_to_global):
        m = rect_plate.RectPlate()
        m.Thickness = thickness
        m.Width = width
        m.Point1 = point.Point(p1)
        m.Point2 = point.Point(p2)
        m.MaterialOriginPoint = origin
        m.WorkpointSlopeDistance = m.Point1.dist(m.Point2)
        m.Member = member.Member(member_number)
        m.Add()
        m.SetTransform(subm_to_global)
        return m
    
    def AddBoltedPlates(mem1, mem2, p1, p2, width, thickness = .5):
        xform = Transform3D.MemberTransform(p1, p2)
        x_dir = xform.GetBasisVectorX()
        y_dir = xform.GetBasisVectorY()
        z_dir = xform.GetBasisVectorZ()
        mid_p1_p2 = Point3D.Interpolate(p1, p2, .5)
        w2 = width / 2.
        to_center_width = -w2 * y_dir
    
        rp1 = add_rect_plate(thickness, width, p1, p2, 'FS', mem1, xform)
    
        h = hole_add.Hole()
        h.Material = [rp1]
        h.pt1 = point.Point(mid_p1_p2 + to_center_width)
        h.face = 'FS Face'
        h.Columns = h.Rows = 1
        h.Locate = 'Center'
        h.BoltDiameter = 1.
        h.BoltType = 'AUTO'
        h.HoleType = 'Standard Round'
        h.Diameter = h.CalculateHoleSize()
        h.SlotLength = h.CalculateSlotLength()
        h.Create()
    
        rp2 = add_rect_plate(thickness, width+1., p1, p2, 'NS', mem2, xform)
    
        hm = hole_add.Hole()
        hm.Material = [rp2]
        hm.Holes = [h]
        hm.BoltDiameter = h.BoltDiameter
        hm.BoltType = h.BoltType
        hm.HoleType = 'Standard Round'
        hm.Diameter = hm.CalculateHoleSize()
        hm.SlotLength = hm.CalculateSlotLength()
        hm.Create()
    
        b = bolt_add.Bolt()
        b.Material = [rp1]
        b.Match = [rp2]
        b.Diameter = h.BoltDiameter
        b.BoltType = h.BoltType
        b.Direction = 'Out'
        b.SuppressWarnings = 'Yes'
        b.IsFieldBolt = 'Field' if mem1 != mem2 else 'Shop'
        b.AddMatch()

