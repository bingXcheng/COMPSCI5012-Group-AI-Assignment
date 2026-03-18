#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    # 对应原 Vue main.vue 的页面
    re_path(r'^main/$', views.main_page, name='main_page'),
    # 学习资源列表页
    re_path(r'^study/$', views.study_page, name='study_page'),
    # 学习记录页
    re_path(r'^record/$', views.record_page, name='record_page'),
    # 删除学习记录
    re_path(r'^record/delete/(?P<record_id>\d+)/$', views.delete_record, name='delete_record'),
    re_path(r'^record/clear/$', views.clear_all_records, name='clear_all_records'),
    # 用户认证相关
    re_path(r'^user/signin/$', views.login_view, name='login'),
    re_path(r'^user/signup/$', views.signup_view, name='signup'),
    re_path(r'^user/logout/$', views.logout_view, name='logout'),
    re_path(r'^user/profile/$', views.profile_view, name='profile'),
    # 资源详情与答题
    re_path(r'^study_detail/$', views.study_detail_page, name='study_detail'),
    re_path(r'^study_detail/record/$', views.study_detail_record, name='study_detail_record'),
    # 兼容旧链接：/study_detail/<id> 形式，自动跳转到 ?id=
    re_path(r'^study_detail/(?P<rid>[^/]+)/$', views.study_detail_legacy, name='study_detail_legacy'),
    # 学习规划相关
    re_path(r'^path/$', views.path_page, name='path_page'),
    re_path(r'^path/create/$', views.path_create, name='path_create'),
    re_path(r'^path/(?P<path_id>\d+)/$', views.path_detail_page, name='path_detail'),
    re_path(r'^path/(?P<path_id>\d+)/edit/$', views.path_edit, name='path_edit'),
    re_path(r'^path/(?P<path_id>\d+)/delete/$', views.path_delete, name='path_delete'),
    re_path(r'^path/(?P<path_id>\d+)/add-resource/$', views.path_add_resource, name='path_add_resource'),
    re_path(r'^path/(?P<path_id>\d+)/remove-resource/(?P<item_id>\d+)/$', views.path_remove_resource, name='path_remove_resource'),
    re_path(r'^path/(?P<path_id>\d+)/toggle-complete/(?P<item_id>\d+)/$', views.path_toggle_complete, name='path_toggle_complete'),
    # 论坛相关
    re_path(r'^forum/$', views.forum_page, name='forum_page'),
    re_path(r'^forum/new/$', views.forum_new_post, name='forum_new_post'),
    re_path(r'^forum/(?P<post_id>\d+)/edit/$', views.forum_edit_post, name='forum_edit_post'),
    re_path(r'^forum/(?P<post_id>\d+)/delete/$', views.forum_delete_post, name='forum_delete_post'),
    # 学习群组相关
    re_path(r'^groups/$', views.groups_page, name='groups_page'),
    re_path(r'^groups/create/$', views.groups_create, name='groups_create'),
    re_path(r'^groups/join/$', views.groups_join, name='groups_join'),
    re_path(r'^groups/join-request/(?P<req_id>\d+)/$', views.groups_handle_join_request, name='groups_handle_join_request'),
    re_path(r'^groups/(?P<group_id>\d+)/$', views.groups_detail_page, name='groups_detail'),
    re_path(r'^groups/(?P<group_id>\d+)/send/$', views.groups_send_message, name='groups_send_message'),
    re_path(r'^groups/(?P<group_id>\d+)/invite/$', views.groups_invite, name='groups_invite'),
    re_path(r'^groups/invite/(?P<invite_id>\d+)/respond/$', views.groups_respond_invite, name='groups_respond_invite'),
    re_path(r'^groups/(?P<group_id>\d+)/kick/(?P<user_id>\d+)/$', views.groups_kick_member, name='groups_kick_member'),
    # Admin dashboard
    re_path(r'^admin-dashboard/$', views.admin_dashboard, name='admin_dashboard'),
    re_path(r'^admin-dashboard/resources/$', views.admin_resources_list, name='admin_resources_list'),
    re_path(r'^admin-dashboard/resources/new/$', views.admin_resource_create, name='admin_resource_create'),
    re_path(r'^admin-dashboard/resource/(?P<resource_id>\d+)/edit/$', views.admin_resource_edit, name='admin_resource_edit'),
    re_path(r'^admin-dashboard/resource/(?P<resource_id>\d+)/json/$', views.admin_resource_json, name='admin_resource_json'),
    re_path(r'^admin-dashboard/resource/(?P<resource_id>\d+)/delete/$', views.admin_resource_delete, name='admin_resource_delete'),
    re_path(r'^admin-dashboard/posts/$', views.admin_posts_list, name='admin_posts_list'),
    re_path(r'^admin-dashboard/posts/new/$', views.admin_post_create, name='admin_post_create'),
    re_path(r'^admin-dashboard/post/(?P<post_id>\d+)/edit/$', views.admin_post_edit, name='admin_post_edit'),
    re_path(r'^admin-dashboard/post/(?P<post_id>\d+)/json/$', views.admin_post_json, name='admin_post_json'),
    re_path(r'^admin-dashboard/groups/$', views.admin_groups_list, name='admin_groups_list'),
    re_path(r'^admin-dashboard/groups/new/$', views.admin_group_create, name='admin_group_create'),
    re_path(r'^admin-dashboard/users/$', views.admin_users_list, name='admin_users_list'),
    re_path(r'^admin-dashboard/users/new/$', views.admin_user_create, name='admin_user_create'),
    re_path(r'^admin-dashboard/paths/$', views.admin_paths_list, name='admin_paths_list'),
    re_path(r'^admin-dashboard/paths/new/$', views.admin_path_create, name='admin_path_create'),
    re_path(r'^admin-dashboard/path/(?P<path_id>\d+)/edit/$', views.admin_path_edit, name='admin_path_edit'),
    re_path(r'^admin-dashboard/path/(?P<path_id>\d+)/json/$', views.admin_path_json, name='admin_path_json'),
    re_path(r'^admin-dashboard/group/(?P<group_id>\d+)/delete/$', views.admin_group_delete, name='admin_group_delete'),
    re_path(r'^admin-dashboard/user/(?P<user_id>\d+)/delete/$', views.admin_user_delete, name='admin_user_delete'),
]

