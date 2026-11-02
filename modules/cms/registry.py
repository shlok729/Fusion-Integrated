from fusion_inventory.modules.registry import Module, NavItem, Permission, RoleGrant

MODULE = Module(
    code='cms',
    label='Complaint Management',
    icon='ExclamationMark',
    base_path='/cms',
    nav_section='Services',
    sort_order=15,
    status='active'
)

NAV_ITEMS = [
    NavItem(label='My Complaints', path='/cms/my-complaints', icon='List', sort_order=1),
    NavItem(label='Handler Queue', path='/cms/handler-queue', icon='Clock', sort_order=2),
    NavItem(label='Escalations', path='/cms/escalations', icon='ExclamationTriangle', sort_order=3)
]

PERMISSIONS = [
    Permission(name='view_complaints', label='View Complaints'),
    Permission(name='create_complaints', label='Create Complaints'),
    Permission(name='edit_complaints', label='Edit Complaints'),
    Permission(name='delete_complaints', label='Delete Complaints')
]

ROLE_GRANTS = {
    'admin': ['view_complaints', 'create_complaints', 'edit_complaints', 'delete_complaints'],
    'user': ['view_complaints', 'create_complaints'],
    'guest': ['view_complaints']
}