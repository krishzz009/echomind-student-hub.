-- Run this in Supabase SQL Editor. It stores one JSON data document per signed-in user.
create table if not exists public.echomind_user_data (
  user_id uuid primary key references auth.users(id) on delete cascade,
  data jsonb not null default '{}'::jsonb,
  updated_at timestamptz not null default now()
);
alter table public.echomind_user_data enable row level security;
drop policy if exists "Users can read own EchoMind data" on public.echomind_user_data;
create policy "Users can read own EchoMind data" on public.echomind_user_data for select to authenticated using (auth.uid() = user_id);
drop policy if exists "Users can insert own EchoMind data" on public.echomind_user_data;
create policy "Users can insert own EchoMind data" on public.echomind_user_data for insert to authenticated with check (auth.uid() = user_id);
drop policy if exists "Users can update own EchoMind data" on public.echomind_user_data;
create policy "Users can update own EchoMind data" on public.echomind_user_data for update to authenticated using (auth.uid() = user_id) with check (auth.uid() = user_id);
