import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {AuthService} from '../auth.service';

@Component({
  selector: 'app-rank',
  templateUrl: './rank.component.html',
  styleUrls: ['./rank.component.css']
})
export class RankComponent implements OnInit {

  configUrl = 'http://127.0.0.1:5000/predictions/';
  configGetUrl = 'http://127.0.0.1:5000/getUser/';
  rateUrl = 'http://127.0.0.1:5000/rateItem/';
  fetchedRecipe = [];
  ratedValue = null;

  constructor(private http: HttpClient, private authService: AuthService) { }

  ngOnInit(): void {
    setTimeout(() => this.getUser(this.authService.uid), 2000 );
  }

  // tslint:disable-next-line:typedef
  getUser(uid){
    console.log(uid);
    this.http.get(this.configGetUrl + uid).subscribe(
      (response: any[]) => this.getRecommendations(response[0]),
      (error) => console.log(error)
    );
  }

  // tslint:disable-next-line:typedef
  getRecommendations(uid) {
    this.http.get(this.configUrl + uid).subscribe(
      (response: any[]) => console.log(this.configUrl + uid, this.fetchedRecipe = response),
      (error) => console.log(error)
    );
  }
  // tslint:disable-next-line:typedef
  rateItem(recipeName) {
    this.http.get(this.rateUrl + recipeName + '/' + this.ratedValue + '/' + this.authService.uid).subscribe(
      (response: any[]) => console.log(response),
      (error) => console.log(error)
    );
  }

}
