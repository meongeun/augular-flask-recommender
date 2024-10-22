import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { NavBarComponent } from './nav-bar/nav-bar.component';
import {RouterModule, Routes} from '@angular/router';
import { DashboardComponent } from './dashboard/dashboard.component';
import {HttpClientModule} from '@angular/common/http';
import {AngularFireModule} from 'angularfire2';
import {AngularFirestoreModule} from 'angularfire2/firestore';
import {AngularFireAuthModule} from 'angularfire2/auth';
import {environment} from '../environments/environment';
import {AuthService} from './auth.service';
import { SignupComponent } from './signup/signup.component';
import {FormsModule} from '@angular/forms';
import { LoginComponent } from './login/login.component';
import { RankComponent } from './rank/rank.component';
import { SearchlectureComponent } from './searchlecture/searchlecture.component';
import { LecNavBarComponent } from './lec-nav-bar/lec-nav-bar.component';

const appRoutes: Routes = [
  {path: '', component: HomeComponent},
  {path: 'navbar', component: NavBarComponent},
  {path: 'dashboard', component: DashboardComponent},
  {path: 'signup', component: SignupComponent},
  {path: 'login', component: LoginComponent},
  {path: 'rank', component: RankComponent},
  {path: 'searchlecture', component: SearchlectureComponent}
];

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    NavBarComponent,
    DashboardComponent,
    SignupComponent,
    LoginComponent,
    RankComponent,
    SearchlectureComponent,
    LecNavBarComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    RouterModule.forRoot(appRoutes),
    AngularFireModule.initializeApp(environment.firebase),
    AngularFirestoreModule,
    AngularFireAuthModule,
    FormsModule
  ],
  providers: [AuthService, DashboardComponent],
  bootstrap: [AppComponent]
})
export class AppModule {}
