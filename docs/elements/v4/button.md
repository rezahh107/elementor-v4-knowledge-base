---
id: elementor.help.button-element
title: Button element
source_url: https://elementor.com/help/button-element/
canonical_url: https://elementor.com/help/button-element/
source_type: official_help
version_scope: editor_v4
last_updated: 2025-07-01
researched_at: 2026-06-23T21:30:05+03:00
evidence_status: completed_with_gaps
storage_status: committed
language: fa
stage_id: KB-004
review_status: unreviewed
provenance_status: document_level_legacy
claim_record: evidence/claims/KB-004-button.yaml
source_record: evidence/sources/SRC-KB-004-01.yaml
image_evidence: evidence/images/KB-004-button.yaml
gap_record: evidence/gaps/KB-004-button.yaml
---

# Button element در Elementor Editor V4

این سند Draft مرحله KB-004 است. منبع فقط صفحه رسمی Elementor Help برای Button element است. این سند peer reviewed نیست.

## دامنه

صفحه رسمی عنوان Button element دارد، تاریخ Last Update آن July 1, 2025 است و صفحه آن را برای Editor v4 معرفی می‌کند. برای Editor v3، منبع رسمی به مقاله جداگانه Button Widget ارجاع می‌دهد.

## هدف

Button element برای ساخت دکمه‌های تعاملی، ایجاد Call to Action و هدایت اقدام کاربر معرفی شده است. مثال صفحه، دکمه‌ای در Hero section است که کاربر را به صفحه ثبت‌نام می‌برد.

## کاربردهای مستند

منبع رسمی این کاربردها را ذکر می‌کند: لینک دادن از دکمه‌های Portfolio gallery به صفحه پروژه یا نمای جزئیات، استفاده در بنر یا پوستر رویداد و وبینار، و نمایش before/after transformation.

## افزودن و حذف

برای افزودن، کاربر در Elementor Editor روی + کلیک می‌کند و سپس element را با کلیک یا drag روی canvas قرار می‌دهد. برای حذف، element روی canvas انتخاب می‌شود و کلید Delete زده می‌شود. متن منبع در همین بخش از واژه widget هم استفاده کرده است، اما عنوان و مسیر صفحه Button element است؛ بنابراین این ناسازگاری به‌عنوان anomaly ثبت شده است.

## مثال رسمی

مقادیر مثال رسمی عبارت‌اند از: Button text برابر Get Started، Link به صفحه مقصد، Width برابر 200، Height برابر 50، Font Family برابر Sora، Font Weight برابر 600، Font Size برابر 16، Background opacity برابر 0 درصد، Border radius برابر 50، Border width برابر 2 و Border color برابر #FFFFFF. این مقادیر فقط example هستند و default محصول محسوب نمی‌شوند.

## General tab

General tab شامل Button text، Link، Open in a new tab و ID است. Button text متن داخل دکمه است. Link با plus sign وارد می‌شود و کلیک بازدیدکننده لینک را باز می‌کند. Open in a new tab فقط وقتی Button لینک دارد مطرح شده است. ID برای tag کردن یک element مشخص در صفحه و لینک دادن به همان element توضیح داده شده است.

## Style tab

Style tab در این صفحه به مقاله‌های جدا برای Layout، Spacing، Size، Position، Typography، Background، Border و Effects ارجاع می‌دهد. جزئیات کامل این خانواده‌ها از همین صفحه نتیجه‌گیری نشده است.

## وضعیت Hover

منبع رسمی Hover را state معرفی می‌کند و می‌گوید ظاهر element می‌تواند بر اساس state تغییر کند. در مثال، از منوی کنار local، Hover انتخاب می‌شود، واژه hover در Classes text box ظاهر می‌شود، رنگ به #FFFFFF و opacity به 100 درصد تغییر می‌کند و Button هنگام mouse hover سفید می‌شود.

## محدوده شواهد

Claimهای documented در فایل claim record ثبت شده‌اند. هیچ observed claim در این commit ساخته نشده چون image evidence فعلاً discovered و not_inspected است. مواردی مثل default واقعی کنترل‌ها، همه stateها، keyboard focus، ARIA، markup، link behavior، responsive behavior، dynamic data، exact plugin version و runtime behavior در gap record باز مانده‌اند.
