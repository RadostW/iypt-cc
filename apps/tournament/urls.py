from django.conf.urls import include, url

from .views import (ADChange, ADCreate, ADDelete, ADMove, AttendeeDataView, BankSettings, DumpView, GroupChange,
                    GroupCreate, GroupsView, JurySettings, OriginChange, OriginCreate, OriginDelete, OriginView,
                    Overview, PhaseChange, PhaseCreate, PhaseDelete, PhaseMove, PhasesView, ProblemChange,
                    ProblemCreate, ProblemDelete, ProblemView, RegistrationSettings, RoleChange, RoleCreate, RoleDelete,
                    RolesView, TemplateSettings, TRoleChange, TRoleCreate, TRoleDelete, TRolesView)

app_name='tournament'

urlpatterns = [
    url(r'^settings/$', Overview.as_view() ,name="overview" ),
    url(r'^settings/templates$', TemplateSettings.as_view() ,name="templates" ),
    url(r'^settings/registration', RegistrationSettings.as_view() ,name="registration" ),
    url(r'^settings/jury', JurySettings.as_view() ,name="jury" ),
    url(r'^settings/bank', BankSettings.as_view() ,name="bank" ),
    url(r'^problems/$', ProblemView.as_view() ,name="problems" ),
    url(r'^problems/edit/(?P<id>\d+)/$', ProblemChange.as_view(), name="change_problem"),
    url(r'^problems/delete/(?P<id>\d+)/$', ProblemDelete.as_view(), name="delete_problem"),
    url(r'^problems/create/$', ProblemCreate.as_view(), name="create_problem"),
    url(r'^origins/$', OriginView.as_view() ,name="origins" ),
    url(r'^origins/edit/(?P<id>\d+)/$', OriginChange.as_view(), name="change_origin"),
    url(r'^origins/delete/(?P<id>\d+)/$', OriginDelete.as_view(), name="delete_origin"),
    url(r'^origins/create/$', OriginCreate.as_view(), name="create_origin"),
    url(r'^participation_data/$', AttendeeDataView.as_view(), name="properties"),
    url(r'^participation_data/edit/(?P<id>\d+)/$', ADChange.as_view(), name="change_property"),
    url(r'^participation_data/delete/(?P<id>\d+)/$', ADDelete.as_view(), name="delete_property"),
    url(r'^participation_data/create/$', ADCreate.as_view(), name="create_property"),
    url(r'^participation_data/move/(?P<id>\d+)/(?P<direction>\w+)/$', ADMove.as_view(), name="move_property"),
    url(r'^phases/$', PhasesView.as_view(), name="phases"),
    url(r'^phases/edit/(?P<id>\d+)/$', PhaseChange.as_view(), name="change_phase"),
    url(r'^phases/delete/(?P<id>\d+)/$', PhaseDelete.as_view(), name="delete_phase"),
    url(r'^phases/create/$', PhaseCreate.as_view(), name="create_phase"),
    url(r'^phases/move/(?P<id>\d+)/(?P<direction>\w+)/$', PhaseMove.as_view(), name="move_phase"),
    url(r'^rights/roles/$', RolesView.as_view(), name="proles"),
    url(r'^rights/roles/edit/(?P<id>\d+)/$', RoleChange.as_view(), name="change_prole"),
    url(r'^rights/roles/delete/(?P<id>\d+)/$', RoleDelete.as_view(), name="delete_prole"),
    url(r'^rights/roles/create/$', RoleCreate.as_view(), name="create_prole"),
    url(r'^rights/team_roles/$', TRolesView.as_view(), name="troles"),
    url(r'^rights/team_roles/edit/(?P<id>\d+)/$', TRoleChange.as_view(), name="change_trole"),
    url(r'^rights/team_roles/delete/(?P<id>\d+)/$', TRoleDelete.as_view(), name="delete_trole"),
    url(r'^rights/team_roles/create/$', TRoleCreate.as_view(), name="create_trole"),
    url(r'^rights/groups/$', GroupsView.as_view(), name="pgroups"),
    url(r'^rights/groups/create/$', GroupCreate.as_view(), name="create_pgroup"),
    url(r'^rights/groups/edit/(?P<id>\d+)/$', GroupChange.as_view(), name="change_pgroup"),
    url(r'^config/dump/$', DumpView.as_view(), name="config_dump"),
]