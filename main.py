import React, { useMemo, useState } from "react";
import { motion } from "framer-motion";
import { Button } from "@/components/ui/button";
import { Card, CardHeader, CardContent, CardTitle, CardDescription } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { Badge } from "@/components/ui/badge";
import { Tabs, TabsList, TabsTrigger, TabsContent } from "@/components/ui/tabs";
import { Accordion, AccordionItem, AccordionTrigger, AccordionContent } from "@/components/ui/accordion";
import { Sheet, SheetContent, SheetHeader, SheetTitle, SheetTrigger } from "@/components/ui/sheet";
import { Separator } from "@/components/ui/separator";
import { Globe, GraduationCap, Users, BookOpen, Calendar, Mail, ArrowRight, Menu, Upload, Download, ClipboardList, Lightbulb, Github, Linkedin, MapPin, Phone } from "lucide-react";

// 단일 파일 React 컴포넌트 — 정보교사 연구회 홈페이지
// Tailwind + shadcn/ui + lucide-react 사용
// 배포: Next.js 또는 Vite + React 환경에서 동작

const NAV = [
  { id: "about", label: "연구회 소개" },
  { id: "programs", label: "프로그램" },
  { id: "events", label: "행사" },
  { id: "resources", label: "자료실" },
  { id: "members", label: "회원/네트워크" },
  { id: "join", label: "가입" },
  { id: "contact", label: "문의" },
];

const PROGRAMS = [
  {
    icon: <Lightbulb className="w-6 h-6" />, 
    title: "AI·데이터 리터러시 연수",
    desc: "고교 정보과 교육과정(2022 개정) 정합의 프로젝트 기반 연수. 평가 루브릭/수행평가 설계 포함.",
    tag: "연수",
  },
  {
    icon: <ClipboardList className="w-6 h-6" />, 
    title: "수업 설계 워크숍",
    desc: "깊이있는 학습과 핵심아이디어 구조에 맞춘 수업·평가 통합 설계 워크숍.",
    tag: "워크숍",
  },
  {
    icon: <BookOpen className="w-6 h-6" />, 
    title: "수업 공유 세미나",
    desc: "동료교사 공개수업·사례발표·피드백 라운드테이블 운영.",
    tag: "세미나",
  },
  {
    icon: <Globe className="w-6 h-6" />, 
    title: "스마트시티 프로젝트",
    desc: "지역사회 연계 캡스톤: IoT, GIS, 데이터 시각화, 시민성 프로젝트.",
    tag: "프로젝트",
  },
];

const EVENTS = [
  { date: "2025-10-18", title: "가을 정기 세미나: 생성형 AI 수업사례 12선", place: "온라인(ZOOM)", link: "#" },
  { date: "2025-11-09", title: "루브릭 마스터클래스(탐구·수행평가)", place: "서울 교원연수원", link: "#" },
  { date: "2025-12-06", title: "연말 코드 페스티벌(학생 작품전)", place: "파트너 고교", link: "#" },
];

const RESOURCES = {
  templates: [
    { name: "배드민턴 탐구 루브릭(예시)", file: "badminton_rubric_v1.xlsx" },
    { name: "AI·디지털 시민성 수업안", file: "ai_digital_citizenship_lesson.md" },
    { name: "프로젝트 평가 체크리스트", file: "project_checklist.pdf" },
  ],
  code: [
    { name: "Folium 지도 예제", repo: "https://github.com/example/folium-map" },
    { name: "Streamlit 대시보드 템플릿", repo: "https://github.com/example/streamlit-dashboard" },
    { name: "Google Apps Script 자동화", repo: "https://github.com/example/gas-automation" },
  ],
};

const TEAM = [
  { name: "대표: 김교사", role: "정보·AI 교육", links: { github: "#", linkedin: "#" } },
  { name: "간사: 이교사", role: "평가·루브릭", links: { github: "#", linkedin: "#" } },
  { name: "연구: 박교사", role: "스마트시티·IoT", links: { github: "#", linkedin: "#" } },
  { name: "홍보: 최교사", role: "디자인·콘텐츠", links: { github: "#", linkedin: "#" } },
];

const FooterLink = ({ children, href = "#" }) => (
  <a href={href} className="text-sm text-muted-foreground hover:text-foreground">
    {children}
  </a>
);

function useNowKST() {
  return useMemo(() => {
    try {
      const now = new Date();
      const kst = new Intl.DateTimeFormat("ko-KR", {
        dateStyle: "full",
        timeStyle: "short",
        timeZone: "Asia/Seoul",
      }).format(now);
      return kst;
    } catch {
      return new Date().toLocaleString();
    }
  }, []);
}

function Header() {
  const [open, setOpen] = useState(false);
  return (
    <header className="fixed top-0 left-0 right-0 z-50 bg-white/70 backdrop-blur border-b">
      <div className="mx-auto max-w-6xl px-4 py-3 flex items-center justify-between">
        <a href="#top" className="flex items-center gap-2">
          <GraduationCap className="w-6 h-6" />
          <span className="font-semibold">정보교사 연구회</span>
        </a>
        <nav className="hidden md:flex items-center gap-6">
          {NAV.map(n => (
            <a key={n.id} href={`#${n.id}`} className="text-sm text-muted-foreground hover:text-foreground">
              {n.label}
            </a>
          ))}
          <a href="#join">
            <Button size="sm">가입하기</Button>
          </a>
        </nav>
        <div className="md:hidden">
          <Sheet open={open} onOpenChange={setOpen}>
            <SheetTrigger asChild>
              <Button variant="outline" size="icon" aria-label="메뉴 열기">
                <Menu className="w-5 h-5" />
              </Button>
            </SheetTrigger>
            <SheetContent side="right" className="w-72">
              <SheetHeader>
                <SheetTitle>메뉴</SheetTitle>
              </SheetHeader>
              <div className="mt-4 grid gap-3">
                {NAV.map(n => (
                  <a key={n.id} href={`#${n.id}`} onClick={() => setOpen(false)} className="text-base">
                    {n.label}
                  </a>
                ))}
                <a href="#join" onClick={() => setOpen(false)}>
                  <Button className="w-full mt-2">가입하기</Button>
                </a>
              </div>
            </SheetContent>
          </Sheet>
        </div>
      </div>
    </header>
  );
}

function Hero() {
  const now = useNowKST();
  return (
    <section id="top" className="relative pt-28 md:pt-32 pb-16 bg-gradient-to-b from-slate-50 to-white">
      <div className="mx-auto max-w-6xl px-4 grid md:grid-cols-2 gap-10 items-center">
        <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }}>
          <Badge className="mb-3" variant="secondary">함께 만드는 미래형 정보교육</Badge>
          <h1 className="text-3xl md:text-5xl font-extrabold leading-tight">
            정보교사 연구회
            <span className="block text-xl md:text-2xl mt-3 font-medium text-muted-foreground">수업·평가·연구·네트워킹의 허브</span>
          </h1>
          <p className="mt-5 text-muted-foreground">
            생성형 AI, 데이터 과학, 소프트웨어 공학, 디지털 시민성까지—현장의 수업을 바꾸고 학생의 성장을 돕는 실천 공동체입니다.
          </p>
          <div className="mt-6 flex flex-wrap gap-3">
            <a href="#join"><Button>지금 가입하기 <ArrowRight className="w-4 h-4 ml-1" /></Button></a>
            <a href="#resources"><Button variant="outline">자료 둘러보기</Button></a>
          </div>
          <p className="mt-6 text-xs text-muted-foreground">현재 시각(대한민국): {now}</p>
        </motion.div>
        <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.8 }} className="md:pl-8">
          <Card className="shadow-lg">
            <CardHeader>
              <CardTitle>우리의 미션</CardTitle>
              <CardDescription>현장 친화, 연구 기반, 학생 성장을 위한 공동체</CardDescription>
            </CardHeader>
            <CardContent className="grid gap-4">
              <div className="flex gap-3 items-start">
                <Users className="w-5 h-5 mt-1" />
                <div>
                  <p className="font-medium">교사 학습공동체 강화</p>
                  <p className="text-sm text-muted-foreground">공개수업·수업나눔·컨설팅으로 전문성의 선순환을 만듭니다.</p>
                </div>
              </div>
              <div className="flex gap-3 items-start">
                <BookOpen className="w-5 h-5 mt-1" />
                <div>
                  <p className="font-medium">수업·평가 혁신</p>
                  <p className="text-sm text-muted-foreground">프로젝트·탐구 중심 설계와 공정한 평가체계를 지원합니다.</p>
                </div>
              </div>
              <div className="flex gap-3 items-start">
                <Globe className="w-5 h-5 mt-1" />
                <div>
                  <p className="font-medium">지역·대학·기업 연계</p>
                  <p className="text-sm text-muted-foreground">스마트시티·산학협력으로 학생의 진로 역량을 확장합니다.</p>
                </div>
              </div>
            </CardContent>
          </Card>
        </motion.div>
      </div>
    </section>
  );
}

function About() {
  return (
    <section id="about" className="py-16">
      <div className="mx-auto max-w-6xl px-4">
        <div className="grid md:grid-cols-2 gap-8 items-start">
          <div>
            <h2 className="text-2xl md:text-3xl font-bold">연구회 소개</h2>
            <p className="mt-4 text-muted-foreground">
              정보교사 연구회는 전국 정보·컴퓨터·AI 교육 교사들이 모여 수업 혁신과 공동 연구를 수행하는 비영리 학습공동체입니다. 2022 개정 교육과정에 기반하여<br className="hidden md:block" />
              프로젝트·탐구·평가를 통합한 수업 생태계를 만들고, 열린 공유 문화를 통해 현장 적용 가능한 도구와 자료를 제공합니다.
            </p>
          </div>
          <Card>
            <CardHeader>
              <CardTitle>핵심 가치</CardTitle>
              <CardDescription>현장성 · 개방성 · 공정성 · 지속가능성</CardDescription>
            </CardHeader>
            <CardContent className="grid sm:grid-cols-2 gap-4">
              {[
                ["현장성", "수업에 바로 쓰이는 실용 자료"],
                ["개방성", "누구나 배우고 나누는 문화"],
                ["공정성", "투명한 평가·검토 프로세스"],
                ["지속가능성", "학생 성장 중심 운영"],
              ].map(([k, v]) => (
                <div key={k} className="rounded-2xl border p-4">
                  <p className="font-medium">{k}</p>
                  <p className="text-sm text-muted-foreground">{v}</p>
                </div>
              ))}
            </CardContent>
          </Card>
        </div>
      </div>
    </section>
  );
}

function Programs() {
  return (
    <section id="programs" className="py-16 bg-slate-50">
      <div className="mx-auto max-w-6xl px-4">
        <div className="flex items-end justify-between gap-4">
          <h2 className="text-2xl md:text-3xl font-bold">프로그램</h2>
          <a href="#contact" className="text-sm text-muted-foreground hover:text-foreground">연수·워크숍 의뢰</a>
        </div>
        <div className="mt-6 grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          {PROGRAMS.map((p, i) => (
            <motion.div key={p.title} initial={{ opacity: 0, y: 8 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }} transition={{ delay: i * 0.05 }}>
              <Card className="h-full">
                <CardHeader className="flex flex-row items-center gap-3">
                  <div className="shrink-0 p-2 rounded-xl bg-slate-100">{p.icon}</div>
                  <div>
                    <CardTitle className="text-base">{p.title}</CardTitle>
                    <CardDescription><Badge variant="outline">{p.tag}</Badge></CardDescription>
                  </div>
                </CardHeader>
                <CardContent>
                  <p className="text-sm text-muted-foreground leading-6">{p.desc}</p>
                </CardContent>
              </Card>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}

function Events() {
  return (
    <section id="events" className="py-16">
      <div className="mx-auto max-w-6xl px-4">
        <h2 className="text-2xl md:text-3xl font-bold">행사</h2>
        <Tabs defaultValue="upcoming" className="mt-6">
          <TabsList>
            <TabsTrigger value="upcoming">예정</TabsTrigger>
            <TabsTrigger value="past">지난 행사</TabsTrigger>
          </TabsList>
          <TabsContent value="upcoming" className="mt-6 grid md:grid-cols-3 gap-6">
            {EVENTS.map(e => (
              <Card key={e.title}>
                <CardHeader>
                  <CardTitle className="text-lg flex items-center gap-2"><Calendar className="w-5 h-5" /> {e.title}</CardTitle>
                  <CardDescription>{e.date} · {e.place}</CardDescription>
                </CardHeader>
                <CardContent>
                  <Button asChild variant="secondary" className="w-full"><a href={e.link}>자세히 보기</a></Button>
                </CardContent>
              </Card>
            ))}
          </TabsContent>
          <TabsContent value="past" className="mt-6">
            <Accordion type="single" collapsible className="w-full">
              {["2025 여름 공개수업 주간", "2025 봄 AI·데이터 심포지엄", "2024 겨울 루브릭 아카데미"].map((t, i) => (
                <AccordionItem key={i} value={`item-${i}`}>
                  <AccordionTrigger>{t}</AccordionTrigger>
                  <AccordionContent className="text-sm text-muted-foreground">
                    자료 및 영상 링크를 정리해 업로드합니다. 회원 전용 아카이브에서 확인하세요.
                  </AccordionContent>
                </AccordionItem>
              ))}
            </Accordion>
          </TabsContent>
        </Tabs>
      </div>
    </section>
  );
}

function Resources() {
  return (
    <section id="resources" className="py-16 bg-slate-50">
      <div className="mx-auto max-w-6xl px-4">
        <div className="flex items-end justify-between">
          <h2 className="text-2xl md:text-3xl font-bold">자료실</h2>
          <p className="text-sm text-muted-foreground">오픈 라이선스(출처 표시) 권장</p>
        </div>
        <div className="mt-6 grid lg:grid-cols-2 gap-6">
          <Card>
            <CardHeader>
              <CardTitle>템플릿 & 양식</CardTitle>
              <CardDescription>수업안, 루브릭, 체크리스트, 가이드</CardDescription>
            </CardHeader>
            <CardContent className="grid gap-3">
              {RESOURCES.templates.map(t => (
                <div key={t.name} className="flex items-center justify-between border rounded-xl p-3">
                  <div className="flex items-center gap-3">
                    <Upload className="w-4 h-4" />
                    <p className="text-sm">{t.name}</p>
                  </div>
                  <Button variant="outline" size="sm">
                    <Download className="w-4 h-4 mr-1" /> 다운로드
                  </Button>
                </div>
              ))}
            </CardContent>
          </Card>
          <Card>
            <CardHeader>
              <CardTitle>코드 & 예제</CardTitle>
              <CardDescription>수업용 레포지토리</CardDescription>
            </CardHeader>
            <CardContent className="grid gap-3">
              {RESOURCES.code.map(c => (
                <div key={c.name} className="flex items-center justify-between border rounded-xl p-3">
                  <div className="flex items-center gap-3">
                    <Github className="w-4 h-4" />
                    <p className="text-sm">{c.name}</p>
                  </div>
                  <Button asChild variant="secondary" size="sm"><a href={c.repo} target="_blank" rel="noreferrer">레포 보기</a></Button>
                </div>
              ))}
            </CardContent>
          </Card>
        </div>
      </div>
    </section>
  );
}

function Members() {
  return (
    <section id="members" className="py-16">
      <div className="mx-auto max-w-6xl px-4">
        <h2 className="text-2xl md:text-3xl font-bold">회원 & 네트워크</h2>
        <p className="mt-3 text-muted-foreground">전국의 정보·컴퓨터·AI 교사, 대학·연구기관, 지역 산업체와 협력합니다.</p>
        <div className="mt-6 grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          {TEAM.map(m => (
            <Card key={m.name}>
              <CardHeader>
                <CardTitle className="text-base">{m.name}</CardTitle>
                <CardDescription>{m.role}</CardDescription>
              </CardHeader>
              <CardContent className="flex gap-3">
                <Button size="icon" variant="outline" asChild><a href={m.links.github}><Github className="w-4 h-4" /></a></Button>
                <Button size="icon" variant="outline" asChild><a href={m.links.linkedin}><Linkedin className="w-4 h-4" /></a></Button>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
}

function Join() {
  return (
    <section id="join" className="py-16 bg-slate-50">
      <div className="mx-auto max-w-6xl px-4">
        <div className="grid lg:grid-cols-2 gap-10 items-start">
          <div>
            <h2 className="text-2xl md:text-3xl font-bold">가입 안내</h2>
            <p className="mt-4 text-muted-foreground">연회비 없는 공개형 커뮤니티를 지향하며, 오프라인 행사 참가비는 실비로 운영합니다. 소속·경력·관심분야를 적어주세요.</p>
            <ul className="mt-4 list-disc pl-5 text-sm text-muted-foreground space-y-2">
              <li>슬랙/디스코드 초대</li>
              <li>월간 뉴스레터/행사 안내</li>
              <li>공개수업 및 실습 워크숍 우선 초대</li>
              <li>자료실 업로드 권한</li>
            </ul>
          </div>
          <Card>
            <CardHeader>
              <CardTitle>가입 신청</CardTitle>
              <CardDescription>간단한 정보를 남겨주세요</CardDescription>
            </CardHeader>
            <CardContent className="grid gap-4">
              <Input placeholder="이름" />
              <Input placeholder="이메일" type="email" />
              <Input placeholder="소속 학교/기관" />
              <Input placeholder="관심 분야 (예: 데이터, AI, IoT, 평가)" />
              <Textarea placeholder="간단한 자기소개 및 기대 사항" rows={4} />
              <Button className="w-full">신청 제출</Button>
              <p className="text-xs text-muted-foreground">제출 시 개인정보 처리방침에 동의한 것으로 간주합니다.</p>
            </CardContent>
          </Card>
        </div>
      </div>
    </section>
  );
}

function Contact() {
  return (
    <section id="contact" className="py-16">
      <div className="mx-auto max-w-6xl px-4">
        <h2 className="text-2xl md:text-3xl font-bold">문의</h2>
        <div className="mt-6 grid md:grid-cols-3 gap-6">
          <Card>
            <CardHeader>
              <CardTitle className="text-base flex items-center gap-2"><Mail className="w-4 h-4" /> 이메일</CardTitle>
            </CardHeader>
            <CardContent className="text-sm text-muted-foreground">contact@infoteachers.org</CardContent>
          </Card>
          <Card>
            <CardHeader>
              <CardTitle className="text-base flex items-center gap-2"><MapPin className="w-4 h-4" /> 주소</CardTitle>
            </CardHeader>
            <CardContent className="text-sm text-muted-foreground">서울특별시 ○○구 ○○로 123, 연구회 사무국</CardContent>
          </Card>
          <Card>
            <CardHeader>
              <CardTitle className="text-base flex items-center gap-2"><Phone className="w-4 h-4" /> 연락처</CardTitle>
            </CardHeader>
            <CardContent className="text-sm text-muted-foreground">02-000-0000 (평일 10:00~17:00)</CardContent>
          </Card>
        </div>
        <Separator className="my-8" />
        <div className="text-xs text-muted-foreground">※ 실제 운영 정보로 교체하세요. 뉴스레터 구독/탈퇴, 개인정보 처리방침 링크 추가 권장.</div>
      </div>
    </section>
  );
}

function Footer() {
  return (
    <footer className="py-10 border-t bg-white">
      <div className="mx-auto max-w-6xl px-4 grid md:grid-cols-4 gap-8">
        <div>
          <div className="flex items-center gap-2 font-semibold"><GraduationCap className="w-5 h-5" /> 정보교사 연구회</div>
          <p className="mt-3 text-sm text-muted-foreground">교사의 성장을 통해 학생의 성장을 이끕니다.</p>
        </div>
        <div className="grid gap-2">
          <p className="font-medium">바로가기</p>
          {NAV.map(n => <FooterLink key={n.id} href={`#${n.id}`}>{n.label}</FooterLink>)}
        </div>
        <div className="grid gap-2">
          <p className="font-medium">정책</p>
          <FooterLink href="#">개인정보 처리방침</FooterLink>
          <FooterLink href="#">이용 약관</FooterLink>
          <FooterLink href="#">오픈 라이선스 안내</FooterLink>
        </div>
        <div className="grid gap-2">
          <p className="font-medium">소셜</p>
          <FooterLink href="#">GitHub</FooterLink>
          <FooterLink href="#">YouTube</FooterLink>
          <FooterLink href="#">Discord</FooterLink>
        </div>
      </div>
      <div className="mx-auto max-w-6xl px-4 mt-8 text-xs text-muted-foreground">© {new Date().getFullYear()} Info Teachers Research Society. All rights reserved.</div>
    </footer>
  );
}

export default function InfoTeachersHome() {
  return (
    <div className="min-h-screen bg-white text-slate-900">
      <Header />
      <main>
        <Hero />
        <About />
        <Programs />
        <Events />
        <Resources />
        <Members />
        <Join />
        <Contact />
      </main>
      <Footer />
    </div>
  );
}
