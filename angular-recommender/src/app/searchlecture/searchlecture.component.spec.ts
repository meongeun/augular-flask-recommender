import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchlectureComponent } from './searchlecture.component';

describe('SearchlectureComponent', () => {
  let component: SearchlectureComponent;
  let fixture: ComponentFixture<SearchlectureComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SearchlectureComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SearchlectureComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
